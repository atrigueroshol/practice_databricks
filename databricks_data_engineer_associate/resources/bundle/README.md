# Bundle de prácticas

En terminal, con Databricks CLI actual y autenticación configurada para tu workspace:

```sh
cd databricks_data_engineer_associate/resources/bundle
databricks auth login --host https://TU_WORKSPACE
databricks bundle validate -t dev --var catalog=TU_CATALOGO,schema=TU_SCHEMA
databricks bundle deploy -t dev --var catalog=TU_CATALOGO,schema=TU_SCHEMA
databricks bundle run -t dev --var catalog=TU_CATALOGO,schema=TU_SCHEMA medallion_job
```

Usa los valores impresos por el notebook 24. Se necesita serverless para las tareas; si no está habilitado, configura compute clásico autorizado en las tareas antes de validar. No guardes tokens ni secretos en Git. Validar resuelve configuración y puede consultar el workspace; no significa haber ejecutado un job.

El DAG incluye Bronze → condición has_rows → Silver → Gold → For each de dos fechas. La rama true habilita Silver. El bucle ejecuta el mismo notebook con stage=dates y process_date={{input}}; un MERGE hace idempotente el registro en job_dates. Mantén concurrency=1 en este ejemplo.

Para test utiliza otro schema exclusivo y `-t test`. El mismo código se promueve con variables distintas. El ejemplo no despliega producción. Para añadir prod, define host/root_path/run_as y recursos autorizados propios antes de activar ese target.

En la UI ejecuta con fail_silver=true: Silver falla y Gold queda bloqueada. Repara la ejecución con fail_silver=false desde Repair run y verifica el resultado Gold. Conserva una captura o notas de estados, duración y tareas reejecutadas.
