-- 1. Количество лиг по странам
SELECT c.name AS country, COUNT(l.id) AS leagues_count
FROM Country c
JOIN League l ON c.id = l.country_id
GROUP BY c.name;

-- 2. Среднее количество голов по лигам
SELECT l.name AS league, AVG(m.home_team_goal + m.away_team_goal) AS avg_goals
FROM Match m
JOIN League l ON m.league_id = l.id
GROUP BY l.name;

-- 3. Победы домашних команд по странам
SELECT c.name AS country, COUNT(*) AS home_wins
FROM Match m
JOIN Country c ON m.country_id = c.id
WHERE m.home_team_goal > m.away_team_goal
GROUP BY c.name;

-- 4. Средний рейтинг игроков по странам
SELECT c.name AS country, AVG(pa.overall_rating) AS avg_rating
FROM Player_Attributes pa
JOIN Player p ON pa.player_api_id = p.player_api_id
JOIN Match m ON m.date = pa.date
JOIN League l ON m.league_id = l.id
JOIN Country c ON l.country_id = c.id
GROUP BY c.name;

-- 5. Средние характеристики команд по сезонам
SELECT SUBSTR(date, 1, 4) AS year,
       AVG(buildUpPlaySpeed) AS avg_speed,
       AVG(defencePressure) AS avg_pressure
FROM Team_Attributes
GROUP BY year
ORDER BY year;

-- 6. Топ-10 команд по голам
SELECT t.team_long_name AS team, SUM(m.home_team_goal + m.away_team_goal) AS total_goals
FROM Match m
JOIN Team t ON m.home_team_api_id = t.team_api_id OR m.away_team_api_id = t.team_api_id
GROUP BY t.team_long_name
ORDER BY total_goals DESC
LIMIT 10;

-- 7. Топ-10 игроков по потенциалу
SELECT p.player_name, MAX(pa.potential) AS max_potential
FROM Player p
JOIN Player_Attributes pa ON p.player_api_id = pa.player_api_id
GROUP BY p.player_name
ORDER BY max_potential DESC
LIMIT 10;

-- 8. Корреляция скорости и рейтинга
SELECT sprint_speed, overall_rating
FROM Player_Attributes
WHERE sprint_speed IS NOT NULL AND overall_rating IS NOT NULL;

-- 9. Средние домашние и выездные голы по сезонам
SELECT season,
       AVG(home_team_goal) AS avg_home_goals,
       AVG(away_team_goal) AS avg_away_goals
FROM Match
GROUP BY season
ORDER BY season;

-- 10. Распределение предпочитаемой ноги игроков
SELECT preferred_foot, COUNT(*) AS count
FROM Player_Attributes
GROUP BY preferred_foot;
