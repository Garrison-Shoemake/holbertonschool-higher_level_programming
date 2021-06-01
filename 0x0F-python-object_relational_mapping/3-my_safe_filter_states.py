#!/usr/bin/python3
""" this script does the same as 2, except protects against SQLI? """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    with db.cursor() as cursor:
        cursor.execute("SELECT * from states\
        WHERE name LIKE BINARY %(name)s \
        ORDER BY states.id ASC", {'name': argv[4]})

        states = cursor.fetchall()

        for state in states:
            print(state)
    cursor.close()
    db.close()
