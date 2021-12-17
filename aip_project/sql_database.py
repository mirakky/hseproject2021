import sqlite3

db = sqlite3.connect('project.db')

sql = ("""CREATE TABLE IF NOT EXISTS products (
    shop TEXT,
    category TEXT,
    name TEXT UNIQUE,
    energy TEXT
)""")
cursor = db.cursor()

cursor.execute(sql)

db.commit()

db.close()

