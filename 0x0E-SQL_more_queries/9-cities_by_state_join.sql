-- this script lists starts use of JOIN
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = state.id;
