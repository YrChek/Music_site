from connect import Engine
import pandas as pd

connect = Engine(username='', password='', host='', port='', database='')
connection = connect.connection()


# Количество исполнителей в каждом жанре
number_performers = connection.execute("""
SELECT Название, COUNT(id_исполнителя) FROM Жанр
JOIN Жанр_Исполнитель ON Жанр.id = Жанр_Исполнитель.id_жанра
GROUP BY Название;""").fetchall()
print(pd.DataFrame(number_performers))

# Количество треков, вошедших в альбомы 2019 - 2020 годов
number_tracks = connection.execute("""
SELECT COUNT(Трек.id) FROM Альбом
JOIN Трек ON Альбом.id = Трек.id_альбома
WHERE Год_выхода BETWEEN 2019 AND 2020;""").fetchall()
print(number_tracks)

# Средняя продолжительность трековв по каждому альбому
average_track_length = connection.execute("""
SELECT Альбом.Название, ROUND(AVG(Длительность), 0) FROM Альбом
JOIN Трек ON Альбом.id = Трек.id_альбома
GROUP BY Альбом.id;""").fetchall()
print(pd.DataFrame(average_track_length))

# Все исполнители, которые не выпустили альбомы в 2020 году
artist_album = connection.execute("""
SELECT Имя FROM Альбом
JOIN Исполнитель_Альбом ON Альбом.id = Исполнитель_Альбом.id_альбома
JOIN Исполнитель ON Исполнитель_Альбом.id_исполнителя = Исполнитель.id
WHERE Год_выхода != 2020
GROUP BY Имя;""").fetchall()
print(pd.DataFrame(artist_album))

# Название сборников, в котором присутствует конкретный исполнитель
artist_collection = connection.execute("""
SELECT Сборник.Название FROM Сборник
JOIN Сборник_Трек ct ON Сборник.id = ct.id_сборника
JOIN Трек ON ct.id_трека = Трек.id
JOIN Альбом ON Трек.id_альбома = Альбом.id
JOIN Исполнитель_Альбом ia ON Альбом.id = ia.id_альбома
JOIN Исполнитель ON ia.id_исполнителя = Исполнитель.id
WHERE Имя IN ('Lx24')
GROUP BY Сборник.Название
;""").fetchall()
print(pd.DataFrame(artist_collection))

# название альбомов,  в которых присутствуют исполнители более 1 жанра
album_style = connection.execute("""
SELECT Альбом.Название FROM Альбом
JOIN Исполнитель_Альбом ia ON ia.id_альбома = Альбом.id
JOIN Исполнитель ON Исполнитель.id = ia.id_исполнителя
JOIN Жанр_Исполнитель ji ON ji.id_исполнителя = Исполнитель.id
JOIN Жанр ON Жанр.id = ji.id_жанра
GROUP BY Альбом.Название
HAVING COUNT(Жанр.Название) != 1
;""").fetchall()
print(pd.DataFrame(album_style))

# Наименование треков, которые не входят в сборники
track_not_collection = connection.execute("""
SELECT Название FROM Трек
LEFT JOIN Сборник_Трек ON Трек.id = Сборник_Трек.id_трека
WHERE Сборник_Трек.id_трека IS NULL
;""").fetchall()
print(pd.DataFrame(track_not_collection))

# Исполнители, написавшие самый короткий по продолжительности трек
small_track = connection.execute("""
SELECT Имя FROM Исполнитель
JOIN Исполнитель_Альбом ON Исполнитель_Альбом.id_исполнителя = Исполнитель.id
JOIN Альбом ON Альбом.id = Исполнитель_Альбом.id_альбома
JOIN Трек ON Альбом.id = Трек.id_альбома
WHERE Длительность IN (SELECT MIN(Длительность) FROM Трек)
;""").fetchall()
print(pd.DataFrame(small_track))

# название альбомов, содержащих наименьшее количество треков
small_album = connection.execute("""
SELECT Альбом.Название FROM Альбом
JOIN Трек ON Альбом.id = Трек.id_альбома
GROUP BY Альбом.Название
HAVING COUNT(Трек.Название) <= (SELECT COUNT(Название) FROM Трек)/(SELECT COUNT(Название) FROM Альбом)
;""").fetchall()
print(pd.DataFrame(small_album))

# Двояко понял предидущий вопрос, поэтому написал еще один запрос
# Название альбома(-ов) содержащего (-их) наименьшее количество треков
small_album_2 = connection.execute("""
SELECT Альбом.Название FROM Альбом
JOIN Трек ON Альбом.id = Трек.id_альбома
GROUP BY Альбом.Название
HAVING COUNT(Трек.Название) <= (SELECT COUNT(Трек.Название) FROM Альбом
 JOIN Трек ON Альбом.id = Трек.id_альбома
  GROUP BY Альбом.Название
   ORDER BY COUNT(Трек.Название)
    LIMIT 1)
;""").fetchall()
print(pd.DataFrame(small_album_2))
