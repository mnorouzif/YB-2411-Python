import mysql.connector

class UserManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def add_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
            print("✅ User added successfully.")
        except mysql.connector.Error as err:
            print(f"❌ Error: {err}")

    def load_users(self):
        query = "SELECT id, username FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
