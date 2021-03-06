#!/usr/bin/python3
""" script that takes in an argument and displays all values """

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
    cur.execute("""SELECT * FROM states
                WHERE name COLLATE latin1_general_cs='{:s}'
                ORDER BY id ASC""".format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
