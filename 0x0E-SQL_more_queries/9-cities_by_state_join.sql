-- List all cities with their corresponding states
-- The result should be sorted by cities.id in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

