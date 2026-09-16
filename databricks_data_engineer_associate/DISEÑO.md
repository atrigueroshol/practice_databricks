# Diseño previo y cobertura

Diseño elaborado antes de generar los notebooks. Referencia: guía oficial aplicable desde el 4 de mayo de 2026, consultada el 16 de septiembre de 2026.

## Estructura

- 01–03: DataFrames, transformaciones, SQL y elección de cómputo.
- 04–11: Delta, historial, esquemas, almacenamiento, Unity Catalog y vistas.
- 12–17: joins, JSON, streaming, Auto Loader, COPY INTO y elección de conectores.
- 18–21: Bronze/Silver/Gold, CDC, SCD1 y SCD2.
- 22–25: pipelines, calidad, Jobs, CI/CD, monitorización y gobierno.
- 26: escenario e-commerce con 18 tareas, sin ejemplos guiados.
- README.md: preparación, índice, requisitos, seguimiento y fuentes.
- resources/: fuentes ejecutables de pipelines y ejemplo de bundle para practicar despliegue.
- tools/: validación estática de formato y estructura.

Cada notebook normal contiene preparación independiente, 2–4 ejemplos, 5–10 ejercicios con celdas vacías, pistas, soluciones completas, 3–5 preguntas originales y reto final sin solución. Se conserva el orden de secciones solicitado: las soluciones de los ejercicios están después de las pistas; el simulacro agrupa sus soluciones al final.

## Matriz de cobertura de la guía vigente

| Área oficial | Prácticas |
|---|---|
| Plataforma y cómputo | 01, 04, 10, 24 |
| Ingesta y carga | 13–17, 24, 26 |
| Transformación y modelado | 02–08, 11–13, 18–23, 26 |
| Lakeflow Jobs | 24, 26 |
| CI/CD | 24 y resources/bundle |
| Diagnóstico, monitorización y optimización | 04, 12, 15, 23, 24 |
| Gobierno y seguridad | 09, 10, 25, 26 |

La lista inicial no nombraba conectores, bundles, diagnóstico, liquid clustering, máscaras ni ABAC: se incluyen dentro de los temas existentes. Las integraciones con sistemas externos tienen una práctica local ficticia y una ampliación condicionada a infraestructura; no se afirma que la simulación ejecute un conector real. No se necesitan datos externos ni se incluyen preguntas oficiales.

## Contratos de ejecución

Notebooks Python con celdas SQL mediante %sql. Cada preparación crea un schema con sufijo único; no afecta a otras prácticas. Las entradas tienen normalmente 12–24 filas, con microlotes menores para simular cambios. Tablas Delta salvo la comparación explícita con Parquet del tema 09. Ficheros y checkpoints en volúmenes de Unity Catalog. Las tablas externas usan una external location separada, nunca una ruta /Volumes. Los checkpoints se conservan al reiniciar una consulta y se renuevan al repetir la preparación.

Las definiciones de Lakeflow se ejecutan en un pipeline: los notebooks 22–23 proporcionan preparación, comparación batch y fuentes separadas. Operaciones privilegiadas se activan explícitamente tras configurar recursos. Las prácticas de Jobs y conectores indican pasos en la interfaz donde son necesarios. No se despliega nada desde este repositorio automáticamente.

## Fuente

[Guía oficial, bloque NEW EXAM GUIDE](https://www.databricks.com/sites/default/files/2026-03/databricks-certified-data-engineer-associate-exam-guide-may-4-2026.pdf). La matriz es una planificación de estudio, no una garantía de aprobar ni un temario oficial sustitutivo.
