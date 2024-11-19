-- Task: List all records from second_table with score >= 10, ordered by score (top first)
-- The results will display both the score and the name, in that order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

