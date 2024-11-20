-- Script to create the database hbtn_0d_2 and user user_0d_2
-- Grants user_0d_2 SELECT privilege on hbtn_0d_2
-- Ensures the script does not fail if the database or user already exists

-- Create the database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2 with password user_0d_2_pwd if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes to privilege tables
FLUSH PRIVILEGES;

