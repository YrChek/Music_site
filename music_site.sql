create table if not exists Жанр (
	ID serial primary key,
	Название text unique);

create table if not exists Исполнитель (
	ID serial primary key,
	Имя text unique);

create table if not exists Альбом (
	ID serial primary key,
	Название text not null unique,
	Год_выхода integer not null);

create table if not exists Трек (
	ID serial primary key,
	Название text not null,
	Длительность integer not null,
	ID_альбома integer references Альбом (ID));
	
create table if not exists Сборник (
	ID serial primary key,
	Название text unique,
	Год_выхода integer not null);
	
create table if not exists Жанр_Исполнитель (
	ID serial primary key,
	ID_жанра integer  references Жанр (ID),
	ID_исполнителя integer references Исполнитель (ID));

create table if not exists Исполнитель_Альбом (
	ID serial primary key,
	ID_исполнителя integer  references Исполнитель (ID),
	ID_альбома integer references Альбом (ID));

create table if not exists Сборник_Трек (
	ID serial primary key,
	ID_сборника integer  references Сборник (ID),
	ID_трека integer references Трек (ID));
	