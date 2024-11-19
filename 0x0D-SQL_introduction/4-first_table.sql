-- Task: Create a table called first_table in the current database
-- The table should have the following columns:
-- - id INT
-- - name VARCHAR(256)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

