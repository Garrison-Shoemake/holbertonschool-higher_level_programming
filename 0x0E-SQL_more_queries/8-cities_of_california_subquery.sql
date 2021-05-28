-- this script lists cities found in a database
-- stats table contains on one record: name = California
-- sort results in ascending order by cities.id
-- no JOIN
SELECT *
FROM hbtn_0d_usa.states
WHERE state_id.cities = 1,
ORDER BY cities.id ASC;
