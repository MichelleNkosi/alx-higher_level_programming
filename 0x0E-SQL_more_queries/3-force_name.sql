-- Script to create the table force_name
-- Ensures the script does not fail if the table already exists

-- Create the table force_name if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

