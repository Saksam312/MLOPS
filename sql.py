from day2.sql_connection import get_connection

def execute(query):
    connection = get_connection()
    if connection is None:
        return None

    cursor=connection.cursor()
    try:
        cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
            result=cursor.fetchall()
        else:
            connection.commit()
            result=cursor.rowcount
        return result
    except Exception as e:
        print("SQL execution failed")
        print(e)
        return None
    finally:
        cursor.close()
        connection.close()

