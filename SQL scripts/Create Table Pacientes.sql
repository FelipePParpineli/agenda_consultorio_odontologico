CREATE TABLE Pacientes (
id_Pacientes int IDENTITY(1,1) PRIMARY KEY,
Sexo varchar(255),
Nome varchar(255) NOT NULL,
Sobrenome varchar(255),
Endereco varchar(255)
);