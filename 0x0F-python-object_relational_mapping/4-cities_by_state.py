#!/usr/bin/python3
""" this script lists all cities from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    with db.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states\
        ON cities.state_id=states.id\
        ORDER BY cities.id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
    cursor.close()
    db.close()
