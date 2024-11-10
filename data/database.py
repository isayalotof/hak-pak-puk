import sqlite3

db = sqlite3.connect('data/data.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_query(
    query_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    query_info TEXT,
    )""")

db.commit()