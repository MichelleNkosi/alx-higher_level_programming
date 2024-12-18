-- Script to create MySQL server user user_0d_1 with all privileges
-- If the user already exists, the script will not fail

-- Create the user user_0d_1 with the password user_0d_1_pwd if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the server to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes to privilege tables
FLUSH PRIVILEGES;

