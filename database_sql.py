import sqlite3

from sqlite3 import Error


# create database and connect to it
def create_connection(db_file):
    """Create connection to database, if if not exist create one."""
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        print("Connected to " + db_file)
        return connection

    except Error:
        print("Cannot connect to " + db_file)

    return connection


def create_table(connection):
    """Create cursor and create table inside of the database."""
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS ranking (
                                name text NOT NULL,
                                score integer NOT NULL)""")
            connection.commit()
            print("Table has been created.")
            return cursor
        except Error:
            print("Cannot create a table")


def insert_data_into_db(connection, cursor, name, score):
    """Take data from user and insert it into the table."""
    try:
        cursor.execute("INSERT INTO ranking VALUES (?, ?)", (name, score))
        connection.commit()
        print("Data has been insert into the table")
    except Error:
        print("Cannot save data into table")


def close_connection(connection):
    """Close connection to the database."""
    connection.close()
    print("Connection has been closed.")


def print_table(cursor):
    cursor.execute("SELECT * FROM ranking")
    print(cursor.fetchall())


def format_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ranking")
    data = (cursor.fetchall())
    return data

# con = create_connection("ranking.db")
# cur = create_table(con)
# name = "Marta"
# score = 60
# insert_data_into_db(con, cur, name, score)
# print_table(cur)
# close_connection(con)
