# Fuente opcional e independiente para un pipeline de AUTO CDC.
# lab.cdc_source = catalog.schema.customer_change_events (preparada por notebook 22).
from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name="customer_changes")
def customer_changes():
    return spark.readStream.table(spark.conf.get("lab.cdc_source"))

dp.create_streaming_table("dim_customers_scd2")
dp.create_auto_cdc_flow(
    target="dim_customers_scd2",
    source="customer_changes",
    keys=["customer_id"],
    sequence_by=F.struct("updated_at", "event_seq"),
    apply_as_deletes=F.expr("op = 'DELETE'"),
    except_column_list=["op", "event_seq"],
    stored_as_scd_type=2
)
# Equivalencia conceptual SQL: SEQUENCE BY STRUCT(updated_at, event_seq).
# El destino expone __START_AT y __END_AT con el tipo de la secuencia.
