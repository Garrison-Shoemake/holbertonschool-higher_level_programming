#!/usr/bin/python3
""" this script lists all cities from a database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    with db.cursor() as cursor:
        cursor.execute("SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id=states.id\
        WHERE states.name LIKE BINARY %(name)s\
        ORDER BY cities.id ASC", {'name': argv[4]})

        states = cursor.fetchall()
        lst = []
        for state in states:
            lst.append(state[0])
        print(", ".join(lst))
    cursor.close()
    db.close()
