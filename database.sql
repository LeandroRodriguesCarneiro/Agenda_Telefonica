CREATE DATABASE Agenda;
USE Agenda;
CREATE TABLE contato(
    Id int AUTO_INCREMENT not null PRIMARY KEY,
    Nome varchar(100) not null,
	Sobrenome varchar(100),
    Email varchar(100),
    Telefone varchar(20) not null
);