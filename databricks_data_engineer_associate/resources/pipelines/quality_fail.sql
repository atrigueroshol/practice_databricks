-- Añadir SOLO para el experimento de fallo del notebook 23.
-- Depende de bronze_quality definido en quality.sql.
CREATE OR REFRESH STREAMING TABLE quality_fail (
  CONSTRAINT valid_amount EXPECT (amount IS NOT NULL AND amount >= 0) ON VIOLATION FAIL UPDATE
)
AS SELECT * FROM STREAM(bronze_quality);
