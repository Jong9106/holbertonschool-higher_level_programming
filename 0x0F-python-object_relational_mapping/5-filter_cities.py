#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all """

import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=user_name,
        passwd=password, db=data_base, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
            FROM cities
            LEFT JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s""", (state_name,))
    query_rows = cur.fetchall()

    try:
        for row in range(len(query_rows)):
            print(query_rows[row][0], end="")
            if query_rows[row + 1] is not None:
                print(', ', end="")
    except:
        pass
        print()

    cur.close()
    conn.close()
