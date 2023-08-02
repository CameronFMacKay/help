import sqlite3
def connect():
    """
        Creates an sqlite 3 connection to the database

        Returns:
            Connection (sqlite3.connect)
    """
    connection = None
    try:
        connection = sqlite3.connect('data.db')
    except Exception as e:
        print(e)
    return connection

def create_db():
    """
        Deletes all tables and creates the database again.
    """
    connection = connect()
    connection.cursor()

    connection.execute(""" CREATE TABLE emails (
        input_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT            
        ) """)
    connection.commit()
    connection.close()

def add_email(data):
    connection = connect()
    connection.cursor()
    connection.execute(
        """ INSERT INTO emails (email)
        VALUES (?)""", (data,)
    )
    connection.commit()
    connection.close()