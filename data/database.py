import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'data.db')

try:
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS user_query(
        query_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        query_info TEXT,
        info TEXT
        )""")
    db.commit()
except sqlite3.OperationalError as e:
    print(f"Ошибка подключения к базе данных: {e}")
