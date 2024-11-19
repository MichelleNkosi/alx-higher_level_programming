-- Task: Update the score of Bob to 10 in the second_table
-- The update should be based on the name field, not the id field

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

