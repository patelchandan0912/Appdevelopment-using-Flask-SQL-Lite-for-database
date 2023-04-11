import sqlite3

conn = sqlite3.connect('database.db')
print("Successfully connected to db")

conn.execute('CREATE TABLE students (name Text, addr TEXT, city TEXT, zip TEXT)')
print("Table created successfully!")

conn.close()