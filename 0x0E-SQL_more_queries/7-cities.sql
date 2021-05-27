-- script that creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT UNIQUE AUTO_GENERATED NOT NULL PRIMARY KEY,
state_id INT NOT NULL FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256)
);
