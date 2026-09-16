# Databricks notebook source
# Notebook de trabajo del bundle. No contiene ejercicios ni soluciones ocultas.
from pyspark.sql import functions as F
from datetime import date

for name, default in [("catalog",""),("schema",""),("stage","bronze"),("fail_silver","false"),("process_date","")]:
    dbutils.widgets.text(name, default)

def ident(value):
    return "`" + value.replace("`", "``") + "`"

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
stage = dbutils.widgets.get("stage")
assert catalog and schema, "Configura variables catalog/schema del bundle"
spark.sql(f"USE CATALOG {ident(catalog)}")
spark.sql(f"USE SCHEMA {ident(schema)}")

if stage == "bronze":
    source = spark.createDataFrame([(i, i%4, float(i*10)) for i in range(1,13)],
                                   "order_id INT, customer_id INT, amount DOUBLE")
    source.write.format("delta").mode("overwrite").saveAsTable("job_bronze")
elif stage == "silver":
    if dbutils.widgets.get("fail_silver").lower() == "true":
        raise ValueError("Fallo didáctico solicitado; cambia fail_silver=false y repara")
    (spark.table("job_bronze").filter("amount >= 0").dropDuplicates(["order_id"])
     .write.format("delta").mode("overwrite").saveAsTable("job_silver"))
elif stage == "gold":
    (spark.table("job_silver").groupBy("customer_id")
     .agg(F.sum("amount").alias("revenue"))
     .write.format("delta").mode("overwrite").saveAsTable("job_gold"))
elif stage == "dates":
    process_date = date.fromisoformat(dbutils.widgets.get("process_date"))
    spark.sql("CREATE TABLE IF NOT EXISTS job_dates (process_date DATE) USING DELTA")
    spark.createDataFrame([(process_date,)], "process_date DATE").createOrReplaceTempView("date_input")
    spark.sql("""MERGE INTO job_dates t USING date_input s ON t.process_date=s.process_date
    WHEN NOT MATCHED THEN INSERT *""")
else:
    raise ValueError("stage debe ser bronze, silver, gold o dates")

dbutils.jobs.taskValues.set(key="rows", value=spark.table("job_" + stage).count())
