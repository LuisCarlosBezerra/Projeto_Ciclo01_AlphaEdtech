import psycopg2
from user_DB import DB_NAME, USER, PASSWORD, HOST, PORT

#-------------------------------------------------------------------------------------------------------
#CONECTANDO AO BANCO DE DADOS
try:
    conexao = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
        )
    print("Conexão estabelecida com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#--------------------------------------------------------------------------------------------------------
#Inserir dados na tabela DOCUMENTO_DIGITAL
def inserir_dados_documento(nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente):
    """
    Função para inserir os dados na tabela documento digital.

    Args:
    nome_agente (str): nome do agente registrado na cédula
    localizacao_fisica (str): código do local onde se encontra a cédula física. ex RA05
    data_contrato (str): data do contrato já em formato padrão de entrada do BD
    valor_credito (float): valor da cédula de crédito
    numero_cedula (str): numero identificador da cédula de crédito
    imagem (str): caminho da imagem
    cliente_id (int): id do cliente, apontando para a tabela cliente


    Returns:
    Sem retorno. A função apenas faz a inserção dos dados no banco de dados.
    """
    try:
        cursor = conexao.cursor()
        # Executar a query com os valores fornecidos
        cursor.execute(f'INSERT INTO Documento_Digital (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente))
        conexao.commit()
        cursor.close()
        
        return True
    except psycopg2.Error as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False
    
#----------------------------------------------------------------------------------------------------------------------------------------- 
#Inserir dados na tabela CLIENTE
def inserir_dados_cliente(nome, cpf, agencia, conta, endereco, data_nascimento):
    """
    Função para inserir dados na tabela cliente.

    Args:
    nome (str): nome do cliente
    cpf (str): cpf do cliente
    agencia (str): agencia onde o cliente tem operação
    conta (float): conta do cliente
    endereco (str): endereço do cliente com rua, bairro, numero, cidade e estado
    data_nascimento: data de nascimento do clientef

    Returns:
    Sem retorno. A função apenas faz a inserção dos dados na tabela cliente.
    """
    try:
        cursor = conexao.cursor()
        # Executar a query com os valores fornecidos
        cursor.execute(f'INSERT INTO Cliente (nome, cpf, agencia, conta, endereco, data_nascimento) VALUES (%s, %s, %s, %s, %s, %s)', (nome, cpf, agencia, conta, endereco, data_nascimento))
        conexao.commit()
        cursor.close()
        
        return True
    except psycopg2.Error as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

#----------------------------------------------------------------------------------------------------------------------------------------- 
#Inserir dados na tabela IMAGEM
def inserir_dados_imagem(nome_imagem, imagem, id_cliente):
    """
    Função para inserir dados na tabela imagem.

    Args:
    nome_imagem (str): nome da imagem
    imagem (str): caminho da imagem
    id_cliente (str): id do cliente da imagem
    
    Returns:
    Sem retorno. A função apenas faz a inserção dos dados na tabela imagem.
    """
    try:
        cursor = conexao.cursor()
        # Executar a query com os valores fornecidos
        cursor.execute(f'INSERT INTO Imagem (nome_imagem, imagem, id_cliente) VALUES (%s, %s, %s)', (nome_imagem, imagem, id_cliente))
        conexao.commit()
        cursor.close()
        
        return True
    except psycopg2.Error as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

#-----------------------------------------------------------------------------------------------------------------------------------------   
#Inserir dados na tabela USUARIO
def inserir_dados_usuario(nome, cpf, user_name, senha):
    """
    Função para inserir dados na tabela usuário.

    Args:
    nome (str): nome do usuário cadastrado
    cpf (str): cpf do usuário cadastrado
    user_name(str): user name usado para login
    senha (str): senha do usuário à ser verificada
    
    Returns:
    Sem retorno. A função apenas faz a inserção dos dados na tabela usuário.
    """
    try:
        cursor = conexao.cursor()
        # Executar a query com os valores fornecidos
        cursor.execute(f'INSERT INTO Usuario (nome, cpf, user_name, senha) VALUES (%s, %s, %s, %s)', (nome, cpf, user_name, senha))
        conexao.commit()
        cursor.close()
        
        return True
    except psycopg2.Error as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

#----------------------------------------------------------------------------------------------------------------------------------------- 
#Inserir dados na tabela APLICACAO_MANIPULA
def inserir_dados_aplicacao(tipo_manipulacao, data_hora, id_usuario, id_documento):
    """
    Função para inserir dados na tabela usuário.

    Args:
    nome (str): nome do usuário cadastrado
    cpf (str): cpf do usuário cadastrado
    user_name(str): user name usado para login
    senha (str): senha do usuário à ser verificada
    
    Returns:
    Sem retorno. A função apenas faz a inserção dos dados na aplicacao.
    """
    try:
        cursor = conexao.cursor()
        # Executar a query com os valores fornecidos
        cursor.execute(f'INSERT INTO Aplicacao_Manipula (tipo_manipulacao, data_hora, id_usuario, id_documento) VALUES (%s, %s, %s, %s)', (tipo_manipulacao, data_hora, id_usuario, id_documento))
        conexao.commit()
        cursor.close()
        
        return True
    except psycopg2.Error as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

if __name__ == "__main__":
    #VARIÁVEIS PARA TESTE INSERIR DOCUMENTO
    nome_agente = 'Luciano Mendes' 
    localizacao_fisica = 'RA05'
    data_contrato = '20/08/2000'
    valor_credito = 20500.57
    numero_cedula = '002458-87'
    id_imagem = 3
    id_cliente = 5

    
    # inserir_dados_imagem('cedula01','c:/users/luis/documentos/cedula01.jpg', 1 )
    # inserir_dados_cliente('Luis Carlos da Silva Bezerra', '002.754.533-40', '5555-5', '22222-0', 'Rua José Carneiro da Silva, n1234', '1985/11/26')
    # inserir_dados_documento(nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente)
    # inserir_dados_usuario('Fulano de Tal', '888.777.222-99', 'user01', 'abc123')
    # inserir_dados_aplicacao('Inserção', '2023/12/15 15:55', 1, 1)
