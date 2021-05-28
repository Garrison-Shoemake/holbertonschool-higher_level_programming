-- this script lists cities found in a database
-- stats table contains on one record: name = California
-- sort results in ascending order by cities.id
-- no JOIN
SELECT id, name
FROM cities
WHERE state_id =
      (SELECT id
      FROM states
      WHERE name = 'California'),
ORDER BY id ASC;
