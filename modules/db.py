import sqlite3

def get_data(database_path, querry):
    conn = sqlite3.connect(database_path)

    cursor = conn.cursor()

    cursor.execute(querry)

    data = cursor.fetchall()

    return data