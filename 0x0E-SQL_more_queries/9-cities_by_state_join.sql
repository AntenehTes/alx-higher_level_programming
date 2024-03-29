-- lists all cities contained in the database hbtn_0d_usa
-- each recors display: cities.id - cities.name - states.name
-- result sorted in ascending order by cities.id
-- use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
