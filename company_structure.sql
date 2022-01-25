create table if not exists Сотрудники (
	Имя text unique not null,
	Отдел text not null,
	Начальник text references Сотрудники (Имя));