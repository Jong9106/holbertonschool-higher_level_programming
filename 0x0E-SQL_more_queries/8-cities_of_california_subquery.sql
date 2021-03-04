-- script that lists all the cities of California that can be found in the database
SELECT id, name FROM cities 
-- Compare id 
WHERE state_id = (SELECT id FROM cities WHERE name ="California")
ORDER BY id ASC;