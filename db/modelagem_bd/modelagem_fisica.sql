CREATE TABLE Cliente (
		id_cliente SERIAL PRIMARY KEY UNIQUE,
		nome VARCHAR NOT NULL,
		cpf VARCHAR NOT NULL UNIQUE,
		agencia VARCHAR NOT NULL,
		conta VARCHAR NOT NULL,
		endereco VARCHAR NOT NULL,
		data_nascimento DATE NOT NULL
);

CREATE TABLE Documento_Digital (
		id_documento SERIAL PRIMARY KEY UNIQUE,
		nome_agente VARCHAR NOT NULL,
		localizacao_fisica VARCHAR NOT NULL,
		data_contrato DATE NOT NULL,
		valor_credito DECIMAL NOT NULL,
		numero_cedula VARCHAR NOT NULL,
		id_imagem INTEGER NOT NULL,
		id_cliente INTEGER NOT NULL
);

CREATE TABLE Usuario (
		id_usuario SERIAL PRIMARY KEY UNIQUE,
		nome VARCHAR NOT NULL,
		cpf VARCHAR NOT NULL UNIQUE,
		user_name VARCHAR NOT NULL UNIQUE,
		senha VARCHAR NOT NULL
);

CREATE TABLE Aplicacao_Manipula (
		id_man SERIAL PRIMARY KEY UNIQUE,
		tipo_manipulacao VARCHAR NOT NULL,
		data_hora TIMESTAMP NOT NULL,
		id_usuario INTEGER NOT NULL,
		id_documento INTEGER NOT NULL
);

CREATE TABLE Imagem (
		id_imagem SERIAL PRIMARY KEY UNIQUE,
		nome_imagem VARCHAR NOT NULL,
		imagem BYTEA NOT NULL
);

ALTER TABLE Aplicacao_Manipula
ADD CONSTRAINT fk_id_documento
FOREIGN KEY (id_documento)
REFERENCES Documento_Digital(id_documento);

ALTER TABLE Aplicacao_Manipula
ADD CONSTRAINT fk_id_usuario
FOREIGN KEY (id_usuario)
REFERENCES Usuario(id_usuario);

ALTER TABLE Documento_Digital
ADD CONSTRAINT fk_id_cliente
FOREIGN KEY (id_cliente)
REFERENCES Cliente(id_cliente);

ALTER TABLE Documento_Digital
ADD CONSTRAINT fk_id_imagem
FOREIGN KEY (id_imagem)
REFERENCES Imagem(id_imagem);
