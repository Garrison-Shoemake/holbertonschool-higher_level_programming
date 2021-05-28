-- this script lists cities found in a database
-- stats table contains on one record: name = California
-- sort results in ascending order by cities.id
-- no JOIN
SELECT id, name
FROM hbtn_0d_usa.cities
WHERE state_id.cities =
 (SELECT id
  FROM hbtn_0d_usa.states
  WHERE name = california),
ORDER BY cities.id ASC;
