-- this script lists cities found in a database
-- stats table contains on one record: name = California
-- sort results in ascending order by cities.id
-- no JOIN
SELECT id, name
FROM cities
WHERE cities =
 (SELECT id
  FROM states
  WHERE name = california),
ORDER BY id ASC;
