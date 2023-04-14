CREATE TABLE Profissionais (
id_Profissionais int IDENTITY(1,1) PRIMARY KEY,
TipoProfissional varchar(255) NOT NULL,
Nome varchar(255) NOT NULL,
Sobrenome varchar(255),
DataNascimento  date,
DataCadastro datetime,
Endereco varchar(255),
Cidade varchar(255),
Estado varchar(255),
CEP varchar(255), 
);