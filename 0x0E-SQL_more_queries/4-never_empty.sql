-- a script that creates the table id_not_null on MySQL server
-- with a default value for the id
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
