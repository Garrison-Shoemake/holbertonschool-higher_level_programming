#!/usr/bin/python3
""" this script lists states that start with capital N """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * from states\
    WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
