import mysql.connector
from db_config import config

def create_connection():
    return mysql.connector.connect(**config)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            age INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_user(name, email, age):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    conn.commit()
    cursor.close()
    conn.close()

def get_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_user(user_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
