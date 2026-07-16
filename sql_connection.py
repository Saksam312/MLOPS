import sqlite3

def get_connection():
    try:
        connection = sqlite3.connect("employee.db")
        cursor = connection.cursor()
        create_table_query =""""
        CREATE TABLE IF NOT EXIST employee (
        id INTEGER NOT NULL PRIMARY KEY ,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
         salary INTEGER NOT NULL
  );
  """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        return connection

    except Exception as e:
        print("Database connection failed")
        print(e)
        return None

