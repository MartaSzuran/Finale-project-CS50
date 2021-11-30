import sqlite3

# to create a table I need to create connection, then cursor and cursor.execute
# cur.execute("""CREATE TABLE ranking (name, score)""")


def open_database(data_base_file):
    # create connection object
    con = sqlite3.connect(data_base_file)
    # create cursor object
    cur = con.cursor()
    return con, cur


def write_into_database(con, cur, name, score):
    cur.execute("INSERT INTO ranking VALUES (?, ?)", (name, score))
    con.commit()


def print_database(cur):
    print(cur.fetchall())


def close_database(con):
    con.close()
