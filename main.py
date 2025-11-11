import sqlite3
import pandas as pd

# === Подключение к базе данных ===
DB_PATH = "database.sqlite"
conn = sqlite3.connect(DB_PATH)

# === Функция для удобного вывода результатов ===
def run_query(query, description):
    print(f"\n📊 {description}")
    df = pd.read_sql(query, conn)
    print(df.head(10))
    print(f"Rows returned: {len(df)}")

# === Выполняем несколько запросов ===
queries = [
    ("Количество лиг по странам", """
        SELECT c.name AS country, COUNT(l.id) AS leagues_count
        FROM Country c
        JOIN League l ON c.id = l.country_id
        GROUP BY c.name;
    """),

    ("Среднее количество голов по лигам", """
        SELECT l.name AS league, AVG(m.home_team_goal + m.away_team_goal) AS avg_goals
        FROM Match m
        JOIN League l ON m.league_id = l.id
        GROUP BY l.name;
    """),

    ("Топ-10 игроков по потенциалу", """
        SELECT p.player_name, MAX(pa.potential) AS max_potential
        FROM Player p
        JOIN Player_Attributes pa ON p.player_api_id = pa.player_api_id
        GROUP BY p.player_name
        ORDER BY max_potential DESC
        LIMIT 10;
    """)
]

# === Запуск всех ===
for desc, sql in queries:
    run_query(sql, desc)

conn.close()
print("\n✅ Все запросы выполнены успешно!")
