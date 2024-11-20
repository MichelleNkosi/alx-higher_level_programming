-- Script to create the database hbtn_0d_usa and the table states
-- Ensures the script does not fail if the database or table already exists

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created database
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-generated unique id, not null
    name VARCHAR(256) NOT NULL          -- Name column, cannot be null
);

