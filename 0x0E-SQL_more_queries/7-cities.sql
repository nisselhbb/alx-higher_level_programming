-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- where id INT unique, auto generated, can’t be null and is a primary key
-- and state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
