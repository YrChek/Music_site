create table if not exists ���� (
	ID serial primary key,
	�������� text unique);

create table if not exists ����������� (
	ID serial primary key,
	��� text unique);

create table if not exists ������ (
	ID serial primary key,
	�������� text not null unique,
	���_������ integer not null);

create table if not exists ���� (
	ID serial unique,
	�������� text not null,
	����������� text references ����������� (���),
	������������ integer not null,
	������ text references ������ (��������),
	constraint pk primary key (��������, �����������));
	
create table if not exists ������� (
	ID serial primary key,
	�������� text unique,
	���_������ integer not null);
	
create table if not exists ����_����������� (
	ID serial primary key,
	ID_����� integer  references ���� (ID),
	ID_����������� integer references ����������� (ID));

create table if not exists �����������_������ (
	ID serial primary key,
	ID_����������� integer  references ����������� (ID),
	ID_������� integer references ������ (ID));

create table if not exists �������_���� (
	ID serial primary key,
	ID_�������� integer  references ������� (ID),
	ID_����� integer references ���� (ID));
	