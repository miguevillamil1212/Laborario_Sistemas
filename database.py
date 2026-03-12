import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="121204",
        database="citas_medicas"
    )
    return conn