-- this script creates a database and adds a user
-- user will have only select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT PRIVILEGE ON 'hbtn_0d_2'@'localhost'.* TO 'user_0d_2'@'localhost';
