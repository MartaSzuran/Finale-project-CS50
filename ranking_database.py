import sqlite3

# create connection object
con = sqlite3.connect("ranking.db")

# create cursor object
cur = con.cursor()

# create table
cur.execute("""CREATE TABLE ranking (name, score)""")


def open_database(cursor, name, score):
    cursor.execute("INSERT INTO ranking VALUES ('name', 'score')")
