from connect import Engine

connect = Engine(username='', password='', host='', port='', database='')
connection = connect.connection()


total_list = [
    ['Миленький ты мой', 'Надежда Кадышева', 'Поп-Фолк', 192, 'С Днем Рождения! 2004', 2004,
     [['Застольные песни', 2020]]],
    ['Варвара', 'БИ-2', 'Русский Рок', 300, 'БИ-2. Grand Collection', 2006,
     [['2500 GOLDEN ROCK HITS', 2019], ['НЕМАЛЕНЬКИЙ СБОРНИК НАШЕГО РОКА (ВЕРСИЯ 2)', 2019]]],
    ['Полковнику никто не пишет', 'БИ-2', 'Русский Рок', 291, 'Сверим сердца', 2021,
     [['20 ВЕК РУССКОГО РОКА VOL.1', 2021]]],
    ['Демобилизация', 'Сектор Газа', 'Панк-Рок', 234, 'Восставший из Ада', 2000,
     [['СЕКТОР ГАЗА - ЛУЧШЕЕ', 2018], ['ПО ВОЛНЕ МОЕЙ ПАМЯТИ 2 ТОМ 32', 2019]]],
    ['Мой сон', 'Легион', 'Русский Рок', 248, 'Маятник времен', 2003,
     [['ЛЕГЕНДЫ НАШЕГО РОКА', 2015]]],
    ['Лирика', 'Сектор Газа', 'Панк-Рок', 260, 'Нажми на газ', 1993,
     [['2500 GOLDEN ROCK HITS', 2019], ['СЕКТОР ГАЗА - ЛУЧШЕЕ', 2018]]],
    ['Моя невеста', 'ТУ-134', 'Поп', 230, 'Украду 2021', 2021,
     [['В МАШИНЕ С МУЗЫКОЙ VOL.215', 2021]]],
    ['Обесточено', 'Artik & Asti', 'Поп', 195, '7(Part2)', 2020,
     [['НОВИЧКИ В ПОПСЕ VOL 3', 2020]]],
    ['Все мимо', 'Artik & Asti', 'Поп', 229, '7(Part2)', 2020,
     [['НОВИЧКИ В ПОПСЕ VOL 3', 2020]]],
    ['Девочка танцуй', 'Artik & Asti', 'Поп', 229, '7(Part2)', 2020,
     [['RECORD SUPER CHART 632', 2020]]],
    ['Уголек', 'Lx24', 'Поп', 211, 'Single 2016', 2016,
     [['РУССКАЯ ДИСКОТЕКА 6', 2018], ['ЗОЛОТОЙ СУПЕРХИТ 2017/2018', 2018]]],
    ['Пятьдесят на пятьдесят', 'Лесоповал', 'Русский Шансон', 186, 'Кормилец', 2000,
     [['ХИТ ПО БЛАТУ', 2000]]],
    ['Фантом', 'Чиж & Co', 'Русский Рок', 212, 'Новый Иерусалим', 1998,
     [['НЕМАЛЕНЬКИЙ СБОРНИК НАШЕГО РОКА (ВЕРСИЯ 2)', 2019]]],
    ['Делай добро', 'АК-47', 'Рэп', 228, 'Баста+ 2015', 2015,
     [['СБОРНИК РУССКОГО РЭПА BY OKAYLIMBO', 2019]]],
    ['Я куплю тебе дом', 'Лесоповал', 'Русский Шансон', 256, 'Я куплю тебе дом', 1991,
     [['ЗВЕЗДЫ ШАНСОНА. ЛУЧШЕЕ. ТОМ 01. ЧАСТЬ 3', 2018]]],
    ['Плакала', 'Kazka', 'Поп', 225, 'Карма 2018', 2018,
     [['UKRAINIAN HITS VOL5 (ROMANTIC)', 2019]]]
]


def insert_author(my_list):
    """Добавление в таблицу Исполнитель"""
    author_list = []
    res = connection.execute("""SELECT Имя FROM Исполнитель;""").fetchall()
    for author in res:
        author_list += author
    for i in my_list:
        if i[1] not in author_list:
            author_list.append(i[1])
            insert = f"INSERT INTO Исполнитель (Имя)" \
                     f"VALUES('{i[1]}');"
            connection.execute(insert)
    print('Добавлены записи в таблицу "Исполнитель"')


def insert_style(my_list):
    """Добавление в таблицу Жанр"""
    style_list = []
    res = connection.execute("""SELECT Название FROM Жанр;""").fetchall()
    for style in res:
        style_list += style
    for i in my_list:
        if i[2] not in style_list:
            style_list.append(i[2])
            insert = f"INSERT INTO Жанр (Название)" \
                     f"VALUES('{i[2]}');"
            connection.execute(insert)
    print('Добавлены записи в таблицу "Жанр"')


def insert_collection(my_list):
    """Добавление в таблицу Сборник"""
    collection_list = []
    res = connection.execute("""SELECT Название FROM Сборник;""").fetchall()
    for collection in res:
        collection_list += collection
    for i in my_list:
        for k in i[-1]:
            if k[0] not in collection_list:
                collection_list.append(k[0])
                insert = f"INSERT INTO Сборник (Название, Год_выхода)" \
                         f"VALUES('{k[0]}', {k[1]});"
                connection.execute(insert)
    print('Добавлены записи в таблицу "Сборник"')


def insert_album(my_list):
    """Добавление в таблицу Альбом"""
    album_list = []
    res = connection.execute("""SELECT Название FROM Альбом;""").fetchall()
    for album in res:
        album_list += album
    for i in my_list:
        if i[4] not in album_list:
            album_list.append(i[4])
            insert = f"INSERT INTO Альбом (Название, Год_выхода)" \
                     f"VALUES('{i[4]}', {i[5]});"
            connection.execute(insert)
    print('Добавлены записи в таблицу "Альбом"')


def insert_track(my_list):
    """Заполнение таблицы Трек"""
    id_track_list = connection.execute("""SELECT id_альбома, Название, Длительность FROM Трек;""").fetchall()
    id_set = set()
    for temp_list in my_list:
        select_id_album = f"SELECT id FROM Альбом " \
                        f"WHERE Название IN ('{temp_list[4]}');"
        id_album = connection.execute(select_id_album).fetchall()
        id_set.add((id_album[0][0], temp_list[0], temp_list[3]))
    result_set = id_set - set(id_track_list)
    if len(result_set) != 0:
        full_insert = str()
        for id_num in result_set:
            insert = f"INSERT INTO Трек (id_альбома, Название, Длительность) " \
                     f"VALUES({id_num[0]}, '{id_num[1]}', {id_num[2]}); "
            full_insert += insert
        connection.execute(full_insert)
        print('Добавлены записи в таблицу "Трек"')
    else:
        print('Записи в таблице "Трек" актуальны')


def insert_collection_track(my_list):
    """Заполнение таблицы Сборник_Трек"""
    collection_track_list = connection.execute("""SELECT id_сборника, id_трека FROM Сборник_Трек;""").fetchall()
    id_set = set()
    for list_from_list in my_list:
        track_select = f"SELECT ID FROM Трек" \
                      f" WHERE Название = '{list_from_list[0]}';"
        id_track = connection.execute(track_select).fetchall()
        for digest in list_from_list[-1]:
            digest_select = f"SELECT ID FROM Сборник" \
                            f" WHERE Название = '{digest[0]}';"
            id_digest = connection.execute(digest_select).fetchall()
            id_set.add((id_digest[0][0], id_track[0][0]))
    result_set = id_set - set(collection_track_list)
    if len(result_set) != 0:
        full_insert = str()
        for id_num in result_set:
            insert = f"INSERT INTO Сборник_Трек (id_сборника, id_трека)" \
                     f"VALUES({id_num[0]}, {id_num[1]}); "
            full_insert += insert
        connection.execute(full_insert)
        print('Добавлены записи в таблицу "Сборник_Трек"')
    else:
        print('Записи в таблице "Сборник_Трек" актуальны')


def insert_style_author(my_list):
    """Заполнение таблицы Жанр_Исполнитель"""
    style_author_list = connection.execute("""SELECT id_жанра, id_исполнителя FROM Жанр_Исполнитель;""").fetchall()
    id_set = set()
    for temp_list in my_list:
        genre_select = f"SELECT ID FROM Жанр" \
                       f" WHERE Название = '{temp_list[2]}';"
        id_style = connection.execute(genre_select).fetchall()
        author_select = f"SELECT ID FROM Исполнитель" \
                        f" WHERE Имя = '{temp_list[1]}';"
        id_author = connection.execute(author_select).fetchall()
        id_set.add((id_style[0][0], id_author[0][0]))
    result_set = id_set - set(style_author_list)
    if len(result_set) != 0:
        full_insert = str()
        for id_num in result_set:
            insert = f"INSERT INTO Жанр_Исполнитель (id_жанра, id_исполнителя)" \
                     f"VALUES({id_num[0]}, {id_num[1]}); "
            full_insert += insert
        connection.execute(full_insert)
        print('Добавлены записи в таблицу "Жанр_Исполнитель"')
    else:
        print('Записи в таблице "Жанр_Исполнитель" актуальны')


def insert_author_album(my_list):
    """Заполнение таблицы Исполнитель_Альбом"""
    author_album_list = connection.execute("""SELECT id_исполнителя, id_альбома 
    FROM Исполнитель_Альбом;""").fetchall()
    id_set = set()
    for temp_list in my_list:
        album_select = f"SELECT ID FROM Альбом" \
                       f" WHERE Название = '{temp_list[4]}';"
        id_album = connection.execute(album_select).fetchall()
        author_select = f"SELECT ID FROM Исполнитель" \
                        f" WHERE Имя = '{temp_list[1]}';"
        id_author = connection.execute(author_select).fetchall()
        id_set.add((id_author[0][0], id_album[0][0]))
    result_set = id_set - set(author_album_list)
    if len(result_set) != 0:
        full_insert = str()
        for id_num in result_set:
            insert = f"INSERT INTO Исполнитель_Альбом (id_исполнителя, id_альбома)" \
                     f"VALUES({id_num[0]}, {id_num[1]}); "
            full_insert += insert
        connection.execute(full_insert)
        print('Добавлены записи в таблицу "Исполнитель_Альбом"')
    else:
        print('Записи в таблице "Исполнитель_Альбом" актуальны')


insert_author(total_list)
insert_style(total_list)
insert_collection(total_list)
insert_album(total_list)
insert_track(total_list)
insert_collection_track(total_list)
insert_style_author(total_list)
insert_author_album(total_list)
