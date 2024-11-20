-- List all cities of California in the database hbtn_0d_usa
-- The cities should be sorted in ascending order by cities.id
-- The database name will be passed as an argument

-- Select cities from the cities table where state_id matches the id of California
-- Get California's id with a subquery from the states table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

