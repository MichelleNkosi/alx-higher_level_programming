-- Script to create the database hbtn_0d_usa and the table cities
-- Ensures the script does not fail if the database or table already exists

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created database
USE hbtn_0d_usa;

-- Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- Auto-generated unique id, not null
    state_id INT NOT NULL,                -- state_id, not null and a foreign key
    name VARCHAR(256) NOT NULL,           -- name column, cannot be null
    FOREIGN KEY (state_id) REFERENCES states(id)   -- Foreign key constraint to states table
);

