/* modelagem_logica: */

CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    cpf VARCHAR,
    user_name VARCHAR,
    senha VARCHAR
);

CREATE TABLE Documento_Digital (
    id INTEGER PRIMARY KEY,
    nome_agente VARCHAR,
    localizacao_fisica VARCHAR,
    data_contrato DATE,
    valor_credito DECIMAL,
    numero_cedula INTEGER,
    arquivo_imagem BYTEA,
    fk_Cliente_id INTEGER
);

CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    cpf VARCHAR,
    agencia VARCHAR,
    conta VARCHAR,
    endereco VARCHAR,
    data_nascimento DATE,
    UNIQUE (cpf, conta)
);

CREATE TABLE Aplicacao_Manipula (
    id INTEGER PRIMARY KEY,
    tipo_manipulacao VARCHAR,
    data_hora TIMESTAMP,
    fk_Usuario_id INTEGER,
    fk_Documento_Digital_id INTEGER
);
 
ALTER TABLE Documento_Digital ADD CONSTRAINT FK_Documento_Digital_2
    FOREIGN KEY (fk_Cliente_id)
    REFERENCES Cliente (id)
    ON DELETE RESTRICT;
 
ALTER TABLE Aplicacao_Manipula ADD CONSTRAINT FK_Aplicacao_Manipula_2
    FOREIGN KEY (fk_Usuario_id)
    REFERENCES Usuario (id);
 
ALTER TABLE Aplicacao_Manipula ADD CONSTRAINT FK_Aplicacao_Manipula_3
    FOREIGN KEY (fk_Documento_Digital_id)
    REFERENCES Documento_Digital (id);