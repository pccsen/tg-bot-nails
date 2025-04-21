import sqlite3

conn = sqlite3.connect("beauty.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        phone TEXT,
        date TEXT,
        time TEXT,
        master TEXT
    )
''')

conn.commit()