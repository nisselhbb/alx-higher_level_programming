-- a script that lists all records of the table second_table
-- but not listing the rows without a name value
-- displaying both score and name respectively
-- records should be ordered by score --> top first
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
