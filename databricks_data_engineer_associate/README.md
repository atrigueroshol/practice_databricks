# Prácticas de Databricks Data Engineer Associate

26 notebooks en español con SQL/PySpark, datos ficticios, **145 ejercicios/tareas con soluciones separadas**, **78 preguntas originales** y retos abiertos. El laboratorio final contiene **18 tareas**, sin ejemplos guiados.

El [diseño previo y la matriz de cobertura](DISEÑO.md) contrastan la colección con la [guía oficial aplicable desde el 4 de mayo de 2026](https://www.databricks.com/sites/default/files/2026-03/databricks-certified-data-engineer-associate-exam-guide-may-4-2026.pdf), consultada el **16 de septiembre de 2026**. Los temas adicionales se integran en los 26 nombres solicitados.

## Cómo empezar

1. Importa los `.ipynb` al Workspace de Databricks o abre este repositorio desde Git folders. No necesitan conversión.
2. Abre 01 y selecciona cómputo de notebook con Unity Catalog. Se recomienda DBR 17.3 LTS o posterior compatible, o serverless cuando admita la operación. Un SQL warehouse por sí solo no ejecuta las celdas PySpark.
3. Ajusta el widget `catalog` a un catálogo existente donde tengas permisos. Si el valor inicial es `hive_metastore`, cambia a un catálogo UC para completar la colección.
4. Ejecuta la preparación una vez. Imprime un schema `dea_NN_<sufijo>` nuevo y aislado. Las celdas de cada notebook se ejecutan en orden; los notebooks son independientes.
5. Completa ejemplos, ejercicios y pistas antes de abrir soluciones. **No uses Run all para estudiar**, porque ejecutaría también las soluciones.
6. Para comparar desde cero, repite toda la preparación y ejemplos, y ejecuta las soluciones en orden en ese nuevo schema. Marca tu progreso al final de este README.

Repetir una celda de INSERT, creación de fichero o incremento salarial puede duplicar datos o fallar porque el objeto existe. Los ejercicios que demuestran idempotencia lo indican expresamente. No hay borrado automático de tus intentos.

## Requisitos y alternativas

| Alcance | Requisito | Alternativa/límite |
|---|---|---|
| Todas | USE CATALOG, CREATE SCHEMA, USE SCHEMA y CREATE TABLE; derechos sobre objetos propios | Usa un schema de prácticas exclusivo asignado por tu administrador y cambia SCHEMA; evita compartir nombres de tabla |
| 04, 09, 10, 14–17, 19, 26 | CREATE VOLUME, READ/WRITE VOLUME | Sustituye la preparación de BASE por un volumen autorizado |
| 09 external | External location de prácticas y CREATE EXTERNAL TABLE; permisos para leer/escribir archivos | Comparación por archivos en volumen; la prueba real de DROP external queda pendiente |
| 10 catálogo | CREATE CATALOG en metastore y almacenamiento configurado | Practica con un catálogo existente |
| 22–23 | Crear/ejecutar pipelines, edición con expectations y CDC cuando se use | Comparación batch local; no equivale a ejecución Lakeflow |
| 24 | CLI autenticada, creación de jobs y serverless para el bundle incluido | Configura cómputo clásico autorizado si serverless no está disponible |
| 25 | Grupos existentes, autoridad para conceder, CREATE FUNCTION/EXECUTE y soporte de políticas | Vistas y simulaciones locales; no sustituyen prueba con otra identidad |
| 25 DENY | Funcionalidad Beta y runtime/privilegios específicos | Ampliación optativa con requisitos enlazados |

La mayoría de ejercicios no necesita administrador. Operaciones privilegiadas usan indicadores como `APPLY_GRANTS=False`; configura los grupos y actívalas solo en tu entorno de prácticas con autoridad. El permiso de crear tablas no sustituye SELECT/MODIFY sobre objetos existentes.

Las fuentes empresariales reales necesitan sistemas y credenciales externos. El tema 17 usa una API ficticia y pasos para configurar Lakeflow Connect/JDBC; **no se afirma haber ejecutado un conector real**.

Se usan tablas Delta salvo la comparación con Parquet de 09. No registres tablas external bajo `/Volumes`: usa una external location. La copia Delta por ruta del volumen de 04 es para inspeccionar archivos, no se registra como external. DROP managed no implica borrado físico instantáneo; sigue el ciclo de recuperación y eliminación de UC.

## Orden recomendado e índice

Sigue 01→26. Para reforzar SQL, puedes completar 03 y 11–13 antes de volver a Delta. Los tiempos incluyen ejercicios, pero no aprovisionamiento ni espera de permisos.

| Notebook | Dificultad | Minutos | Temas cubiertos |
|---|---|---:|---|
| [Spark y DataFrames](Spark y DataFrames.ipynb) | Básico | 45 | DataFrames, evaluación perezosa, cómputo |
| [Transformaciones PySpark](Transformaciones PySpark.ipynb) | Básico | 55 | Limpieza, tipos y deduplicación |
| [Spark SQL](Spark SQL.ipynb) | Básico | 50 | SQL, CTE, agregaciones, UNION |
| [Fundamentos físicos y operaciones de Delta](Fundamentos físicos y operaciones de Delta.ipynb) | Básico | 75 | DDL/DML, ACID, archivos, clustering |
| [INSERT, UPDATE y DELETE](INSERT, UPDATE y DELETE.ipynb) | Básico | 50 | INSERT, UPDATE, DELETE, idempotencia |
| [MERGE de clientes](MERGE de clientes.ipynb) | Intermedio | 75 | Upsert, claves y secuencia |
| [Historial, time travel y RESTORE](Historial, time travel y RESTORE.ipynb) | Intermedio | 65 | Versiones, RESTORE, retención |
| [Schema enforcement y evolution](Schema enforcement y evolution.ipynb) | Intermedio | 55 | Enforcement y evolución |
| [Tablas managed y external; Delta y Parquet](Tablas managed y external; Delta y Parquet.ipynb) | Intermedio | 75 | Managed/external, Parquet, LOCATION, DROP |
| [Unity Catalog: catálogo, schema y objetos](Unity Catalog: catálogo, schema y objetos.ipynb) | Intermedio | 65 | Jerarquía UC, volúmenes, privilegios |
| [Vistas persistentes y temporales](Vistas persistentes y temporales.ipynb) | Básico | 45 | Vistas, alcance y snapshots |
| [Joins, agregaciones y diagnóstico](Joins, agregaciones y diagnóstico.ipynb) | Intermedio | 70 | Joins, broadcast, skew, spill y métricas |
| [JSON, struct, array y datos semiestructurados](JSON, struct, array y datos semiestructurados.ipynb) | Intermedio | 55 | JSON, struct, array y explode |
| [Batch frente a streaming incremental](Batch frente a streaming incremental.ipynb) | Intermedio | 60 | Batch, streaming y checkpoints |
| [Structured Streaming: estado y ventanas](Structured Streaming: estado y ventanas.ipynb) | Intermedio | 75 | Ventanas, watermark y estado |
| [Auto Loader](Auto Loader.ipynb) | Intermedio | 75 | cloudFiles, rescate y evolución |
| [COPY INTO y selección de ingesta](COPY INTO y selección de ingesta.ipynb) | Intermedio | 65 | COPY INTO, conectores, REST/JDBC |
| [Arquitectura Medallion](Arquitectura Medallion.ipynb) | Intermedio | 65 | Bronze/Silver/Gold y contratos |
| [CDC y Change Data Feed](CDC y Change Data Feed.ipynb) | Intermedio | 70 | CDF y eventos de cambios |
| [SCD Type 1](SCD Type 1.ipynb) | Intermedio | 60 | SCD1 y secuencia |
| [SCD Type 2 e intervalos de validez](SCD Type 2 e intervalos de validez.ipynb) | Examen | 90 | SCD2 e intervalos |
| [Lakeflow Spark Declarative Pipelines](Lakeflow Spark Declarative Pipelines.ipynb) | Intermedio | 90 | Pipelines, MV y AUTO CDC |
| [Calidad y expectations](Calidad y expectations.ipynb) | Intermedio | 75 | EXPECT, DROP, FAIL y recuperación |
| [Lakeflow Jobs, CI/CD y operación](Lakeflow Jobs, CI/CD y operación.ipynb) | Examen | 110 | Jobs, Git, bundles, triggers y diagnóstico |
| [Permisos, máscaras y gobierno](Permisos, máscaras y gobierno.ipynb) | Examen | 90 | Permisos, máscaras, filtros, ABAC y DENY |
| [26_full_exam_lab](26_full_exam_lab.ipynb) | Examen | 180–240 | Escenario integral y decisiones |

## Cómo están organizados

01–25: tema, objetivos, conceptos, preparación, 2–4 ejemplos, 5–10 ejercicios con celdas vacías, pistas, soluciones completas, 3 preguntas originales con cuatro opciones y explicación, y reto sin solución. Se conserva el orden solicitado: soluciones después de pistas y antes de preguntas/reto.

26: escenario y fuentes, 18 tareas, pistas, preguntas de decisión y reto; todas las soluciones y respuestas quedan al final. No hay ejemplos guiados. Las preguntas no son oficiales ni proceden de dumps.

## Ejecución de pipelines y Jobs

- [medallion.py](resources/pipelines/medallion.py): fuente del pipeline 22. Configura `lab.source_table` y catálogo/schema destino con los valores impresos.
- [auto_cdc.py](resources/pipelines/auto_cdc.py): pipeline independiente con `lab.cdc_source` y otro schema.
- [quality.sql](resources/pipelines/quality.sql): fuente del pipeline 23 para observar, descartar y conservar cuarentena.
- [quality_fail.sql](resources/pipelines/quality_fail.sql): añadir después para provocar el fallo esperado.
- [Bundle](resources/bundle/README.md): comandos de validación, despliegue y ejecución dev/test.

Adjunta únicamente los archivos fuente indicados a cada pipeline. No ejecutes `pyspark.pipelines` en un notebook interactivo ni adjuntes todos los notebooks del curso a un pipeline. Separa preparación, actualización del servicio y verificación; activa `RUN_PIPELINE_CHECKS`/`RUN_CDC_CHECKS` después de ejecutar el servicio.

El bundle utiliza notebooks de trabajo sin ejercicios. Para automatizar tus propias soluciones, extrae el código operativo y parametriza un schema persistente. No programes la preparación de estudio que genera otro UUID en cada ejecución.

## Validación y límites

Se ha verificado localmente formato JSON, estructura, separación de soluciones, celdas de intento vacías, ausencia de salidas guardadas, sintaxis Python y expectativas numéricas de datos ficticios.

```sh
python databricks_data_engineer_associate/tools/validate_notebooks.py
```

En Windows puedes sustituir `python` por `py -3.14`. El validador solo usa biblioteca estándar.

**No se han ejecutado los notebooks en Databricks ni validado/desplegado el bundle contra un workspace.** La revisión estática no prueba resolución SQL, permisos, disponibilidad de funcionalidades ni ejecución distribuida. Realiza el primer recorrido por celdas.

## Repetición y limpieza

Conserva checkpoints entre reintentos de la misma consulta. Una preparación nueva crea otro schema y rutas; no reutilices estado para cualquier plan diferente. Los datos persisten para inspeccionar historial.

Al terminar, revisa el schema impreso y elimina únicamente tus objetos de prácticas desde Catalog Explorer. Los archivos external requieren limpieza separada en su ruta autorizada. Detén consultas activas y pausa/elimina jobs y pipelines que ya no uses. No se incluye borrado masivo automático.

## Seguimiento

### 01_spark_dataframe_basics

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 02_pyspark_transformations

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 03_spark_sql

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 04_delta_tables_basics

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 05_delta_insert_update_delete

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 06_delta_merge

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 07_delta_history_time_travel

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 08_delta_schema_enforcement_evolution

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 09_managed_vs_external_tables

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 10_unity_catalog

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 11_views_and_temp_views

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 12_joins_and_aggregations

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 13_complex_types_json_struct_array

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 14_streaming_basics

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 15_structured_streaming

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 16_auto_loader

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 17_copy_into

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 18_medallion_architecture

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 19_cdc

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 20_scd_type_1

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 21_scd_type_2

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 22_lakeflow_declarative_pipelines

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 23_data_quality_expectations

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 24_lakeflow_jobs

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 25_permissions_and_governance

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

### 26_full_exam_lab

- [ ] Completado
- [ ] Necesito repasar
- [ ] Dominado

## Fuentes oficiales

- [Guía de examen: bloque NEW EXAM GUIDE](https://www.databricks.com/sites/default/files/2026-03/databricks-certified-data-engineer-associate-exam-guide-may-4-2026.pdf).
- [Tablas managed](https://docs.databricks.com/aws/en/tables/managed) y [ciclo de almacenamiento](https://docs.databricks.com/aws/en/data-governance/unity-catalog/object-storage-lifecycle).
- [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema) y [streaming Delta](https://docs.databricks.com/aws/en/structured-streaming/delta-lake).
- [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/).
- [Pipelines Python](https://docs.databricks.com/aws/en/ldp/developer/python-dev), [AUTO CDC](https://docs.databricks.com/aws/en/ldp/developer/ldp-python-ref-apply-changes), [expectations](https://docs.databricks.com/aws/en/ldp/expectations).
- [Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/reference) y [CLI](https://docs.databricks.com/aws/en/dev-tools/cli/bundle-commands).
- [Máscaras y filtros](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply) y [alcance de DENY](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/deny-policies).

Los enlaces de documentación son AWS. Azure/GCP comparten conceptos centrales, pero cambian URI, permisos cloud y disponibilidad.
