import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# === 1. Подключение к SQLite ===
sqlite_conn = sqlite3.connect("database.sqlite")

# === 2. Подключение к PostgreSQL ===
# ⚠️ Замени пароль и имя пользователя, если другие
engine = create_engine("postgresql://postgres:NewPassword123@localhost:5432/football_db")

# === 3. Получаем список таблиц из SQLite ===
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';", sqlite_conn)

# === 4. Цикл по всем таблицам ===
for table_name in tables['name']:
    df = pd.read_sql(f"SELECT * FROM {table_name}", sqlite_conn)
    df.to_sql(table_name.lower(), engine, index=False, if_exists='replace')  # таблицы будут в нижнем регистре
    print(f"✅ Импортирована таблица: {table_name} ({len(df)} строк)")

sqlite_conn.close()
print("\n🎯 Перенос завершён успешно!")
