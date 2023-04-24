CREATE TABLE Consultas (
id_Consultas int IDENTITY(1,1) PRIMARY KEY,
nome_Profissional varchar(255) NOT NULL,
nome_Paciente varchar(255) NOT NULL,
Horario varchar(255) NOT NULL
);