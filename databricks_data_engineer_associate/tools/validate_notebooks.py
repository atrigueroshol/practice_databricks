"""Validación estática sin dependencias; no ejecuta Spark ni sustituye Databricks."""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
expected = [
"spark_dataframe_basics","pyspark_transformations","spark_sql","delta_tables_basics",
"delta_insert_update_delete","delta_merge","delta_history_time_travel",
"delta_schema_enforcement_evolution","managed_vs_external_tables","unity_catalog",
"views_and_temp_views","joins_and_aggregations","complex_types_json_struct_array",
"streaming_basics","structured_streaming","auto_loader","copy_into",
"medallion_architecture","cdc","scd_type_1","scd_type_2",
"lakeflow_declarative_pipelines","data_quality_expectations","lakeflow_jobs",
"permissions_and_governance","full_exam_lab"]
files = sorted(ROOT.glob("*.ipynb"))
assert [f.stem for f in files] == [f"{i:02}_{name}" for i,name in enumerate(expected,1)]
counts = {"notebooks":0,"code_cells":0,"python_cells":0,"sql_cells":0,"exercises":0,"solutions":0}
for number, path in enumerate(files,1):
    nb = json.loads(path.read_text(encoding="utf-8"))
    assert nb["nbformat"] == 4 and nb["nbformat_minor"] == 5, path
    text = "\n".join("".join(c["source"]) for c in nb["cells"])
    assert "\ufffd" not in text and "\u00c3\u00b3" not in text, f"Codificación: {path}"
    for header in ["# Tema:", "## Objetivos", "## Conceptos importantes para el examen"]:
        assert header in text, (path,header)
    ids = set()
    exercises, solutions = [], []
    for index, cell in enumerate(nb["cells"]):
        assert cell["id"] not in ids
        ids.add(cell["id"])
        assert isinstance(cell["source"],list) and cell["source"]
        source = "".join(cell["source"])
        assert cell["cell_type"] in {"code","markdown"}
        if cell["cell_type"] != "code":
            continue
        counts["code_cells"] += 1
        assert cell["execution_count"] is None and cell["outputs"] == []
        tags = cell["metadata"].get("tags",[])
        if "exercise" in tags:
            exercises.append(index)
            # Celdas de intento realmente vacías: solo comentarios.
            assert all(not line.strip() or line.lstrip().startswith("#") for line in source.splitlines())
        if "solution" in tags:
            solutions.append(index)
        if source.lstrip().startswith("%sql"):
            counts["sql_cells"] += 1
            assert len(source.splitlines()) > 1
        else:
            ast.parse(source, filename=f"{path.name}:cell{index}")
            counts["python_cells"] += 1
    assert len(exercises) == len(solutions)
    assert max(exercises) < min(solutions), f"Soluciones intercaladas: {path}"
    if number < 26:
        assert 5 <= len(exercises) <= 10
        for section in range(1,7):
            assert f"## PARTE {section} -" in text, (path,section)
        assert 3 <= text.count("### Pregunta ") <= 5
        assert nb["cells"][-1]["metadata"]["tags"] == ["challenge"]
    else:
        assert 15 <= len(exercises) <= 20
        assert "EJEMPLOS GUIADOS" not in text
        assert text.count("### TAREA ") == 18
    counts["notebooks"] += 1
    counts["exercises"] += len(exercises)
    counts["solutions"] += len(solutions)

for path in ROOT.glob("resources/**/*.py"):
    ast.parse(path.read_text(encoding="utf-8"),filename=str(path))

# Oráculos independientes para las expectativas numéricas de los datos ficticios.
active_data = [i for i in range(1,19) if i%3==0 and i%4!=0 and 30000+i*1500>40000]
assert active_data == [9,15,18]
assert sum(i*10 for i in range(1,19)) == 1710
assert sum(i*10 for i in range(1,12)) == 660
assert sum(i*10 for i in range(1,13)) == 780
assert sum((i%3+1)*(((i-1)%6+1)*10) for i in range(1,25)) == 1600

print(json.dumps(counts,ensure_ascii=False,indent=2))
print("Correcto: formato, orden, celdas vacías, sintaxis Python y oráculos locales.")
print("Pendiente: ejecución SQL/Spark, permisos UC, pipelines y bundle en Databricks.")
