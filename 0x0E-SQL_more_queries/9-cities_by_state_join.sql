-- this script lists starts use of JOIN
SELECT cities.id, cities.name, state.name
FROM cities
JOIN states
ON cities.state_id = state.id;
