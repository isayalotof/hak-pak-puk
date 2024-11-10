import os
import sqlite3

# Получаем абсолютный путь к текущей директории (data)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к файлу базы данных
db_path = os.path.join(base_dir, 'data.db')

# Выводим путь к базе данных для проверки
print(f"Путь к базе данных: {db_path}")

# Подключаемся к базе данных
try:
    db = sqlite3.connect(db_path)
    c = db.cursor()

    # Создаём таблицу, если её нет
    c.execute("""CREATE TABLE IF NOT EXISTS user_query(
        query_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        query_info TEXT,
        info TEXT
        )""")

    db.commit()
except sqlite3.OperationalError as e:
    print(f"Ошибка подключения к базе данных: {e}")
