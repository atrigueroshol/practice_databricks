# Fuente de Lakeflow: adjuntar a un pipeline, no ejecutar como notebook interactivo.
# Configuración requerida: lab.source_table = catalog.schema.pipeline_input
from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name="bronze_orders")
def bronze_orders():
    return spark.readStream.table(spark.conf.get("lab.source_table"))

@dp.table(name="silver_orders")
@dp.expect_or_drop("valid_amount", "amount IS NOT NULL AND amount >= 0")
@dp.expect_or_drop("valid_id", "order_id IS NOT NULL")
def silver_orders():
    return spark.readStream.table("bronze_orders")

@dp.materialized_view(name="gold_customers")
def gold_customers():
    return (spark.read.table("silver_orders").groupBy("customer_id")
            .agg(F.sum("amount").alias("revenue"), F.count("*").alias("orders")))
