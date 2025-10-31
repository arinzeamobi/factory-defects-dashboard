-- Query 1: Top Defects by Type
SELECT defect_type, SUM(defect_count) as total_defects
FROM defects
GROUP BY defect_type
ORDER BY total_defects DESC;

-- Query 2: Yield % per Line
SELECT line, 
  (1 - SUM(defect_count)::FLOAT / SUM(produced_count)) * 100 as yield_percent
FROM defects
GROUP BY line
ORDER BY yield_percent DESC;

-- Query 3: Scrap Cost by Month and Product
SELECT 
  EXTRACT(MONTH FROM date) as month,
  product,
  SUM(scrap_cost) as total_scrap_cost
FROM defects
GROUP BY month, product
ORDER BY month, total_scrap_cost DESC;