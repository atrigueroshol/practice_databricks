-- Adjuntar a un pipeline configurado con lab.source_table.
-- Modo de publicación actual: se resuelven nombres en el catálogo/schema destino.
CREATE OR REFRESH STREAMING TABLE bronze_quality
AS SELECT * FROM STREAM(${lab.source_table});

CREATE OR REFRESH STREAMING TABLE quality_observe (
  CONSTRAINT valid_amount EXPECT (amount IS NOT NULL AND amount >= 0)
)
AS SELECT * FROM STREAM(bronze_quality);

CREATE OR REFRESH STREAMING TABLE quality_drop (
  CONSTRAINT valid_amount EXPECT (amount IS NOT NULL AND amount >= 0) ON VIOLATION DROP ROW
)
AS SELECT * FROM STREAM(bronze_quality);

CREATE OR REFRESH MATERIALIZED VIEW quality_quarantine
AS SELECT * FROM bronze_quality WHERE amount IS NULL OR amount < 0;

CREATE OR REFRESH MATERIALIZED VIEW quality_summary
AS SELECT customer_id, SUM(amount) AS revenue FROM quality_drop GROUP BY customer_id;
