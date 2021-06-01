#!/usr/bin/python3
""" this script will take a name and returns values with that name """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * from states\
    WHERE name LIKE BINARY '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
