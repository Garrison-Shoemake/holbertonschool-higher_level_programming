#!/usr/bin/python3
""" this script lists states from a database """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv


    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * from states ORDER by states.id")
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
