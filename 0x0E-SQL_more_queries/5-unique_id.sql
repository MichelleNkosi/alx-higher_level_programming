-- Script to create the table unique_id
-- Ensures the script does not fail if the table already exists

-- Create the table unique_id if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

