from connect import Engine

connect = Engine(username='', password='', host='', port='', database='')
connection = connect.connection()


album_release_year = connection.execute("""
SELECT Название, Год_выхода FROM Альбом
WHERE Год_выхода = 2018;""").fetchall()
print(album_release_year)

long_track = connection.execute("""
SELECT Название, Длительность FROM Трек
ORDER BY Длительность DESC
LIMIT 1;""").fetchall()
print(long_track)

track_duration = connection.execute("""
SELECT Название, Длительность FROM Трек
WHERE Длительность >= 210;""").fetchall()
print(track_duration)

collection_release_year = connection.execute("""
SELECT Название, Год_выхода FROM Сборник
WHERE Год_выхода BETWEEN 2018 AND 2020;""").fetchall()
print(collection_release_year)

name = connection.execute("""
SELECT Имя FROM Исполнитель
WHERE Имя NOT LIKE'%% %%';""").fetchall()
print(name)

name = connection.execute("""
SELECT Название FROM Трек
WHERE Название ILIKE'мой %%' OR Название ILIKE'%% мой';""").fetchall()
print(name)
