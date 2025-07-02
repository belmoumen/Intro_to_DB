import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server (not to a specific database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dixhuitcent1@"
        )

        cursor = connection.cursor()

        # Try to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("❌ Error: Could not connect to the database.")
        print(f"Details: {err}")

    finally:
        # Close the cursor and connection if they were opened
        try:
            cursor.close()
            connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
