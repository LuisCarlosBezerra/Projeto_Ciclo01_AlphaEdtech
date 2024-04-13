from user_DB import DB_NAME, USER, PASSWORD, HOST, PORT
import psycopg2
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

try:
    conexao = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
    print('Conexão estabelecida com sucesso!')
except Exception as error:
    print(f'Falha ao conectar. Erro: {error}')


#--------------------------------TABELA IMAGEM------------------------------------------
#inserir imagem
def inserir_imagem(image_path, image_name):
    """
    Inserts an image into the database.

    Args:
        image_path (str): Path of the image file.
        image_name (str): Name of the image.

    Returns:
        bool: True if insertion is successful, False otherwise.
    """
    try:
        with conexao.cursor() as cursor:
            with open(image_path, "rb") as image_file:
                img = image_file.read()

                cursor.execute(
                    f"""
                    INSERT INTO imagem (nome_imagem, imagem) 
                        VALUES ('{image_name}', {psycopg2.Binary(img)});
                    """
                )

            print("INFO: Inserção realizada com sucesso.")
            conexao.commit()
            return True
    except Exception as e:
        print("INFO: Erro ao inserir imagem no banco de dados.")
        print(f"ERROR: {e}")
        conexao.rollback()
        return False
#ler imagem
def ler_imagem(image_id):
    """
    Reads an image from the database and displays it.

    Args:
        image_id (int): ID of the image to be read.

    """
    try:
        with conexao.cursor() as cursor:
            sql = "SELECT nome_imagem, imagem FROM imagem WHERE id_imagem = %s"
            cursor.execute(sql, (image_id,))
            registro = cursor.fetchone()

            if registro is not None:
                nome_imagem, dados_imagem = registro
                imagem_stream = BytesIO(dados_imagem)
                imagem = Image.open(imagem_stream)
                nome_arquivo_saida = f"imagem_recuperada_{image_id}.jpg"
                plt.imshow(imagem)
                plt.show()
                print(
                    f"INFO: Imagem {nome_imagem} recuperada e salva como {nome_arquivo_saida}"
                )
            else:
                print("INFO: Nenhuma imagem encontrada com o ID especificado.")
    except Exception as e:
        print("INFO: Erro ao ler imagem do banco de dados.")
        print(f"ERROR: {e}")

#--------------------------------TABELA CLIENTE------------------------------------------
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
        with conexao.cursor() as cursor:
            cursor.execute(f'INSERT INTO Cliente (nome, cpf, agencia, conta, endereco, data_nascimento) VALUES (%s, %s, %s, %s, %s, %s)', (nome, cpf, agencia, conta, endereco, data_nascimento))
            conexao.commit()
            cursor.close()
            print("Dados inseridos na tabela CLIENTE")
            return True
        
    except Exception as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False
    
#Consultar dados por CLIENTE
def consultar_cliente_id(id_cliente):
    """
    Consulta cliente por id

    Args:
        id_cliente(int): ID do cliente à ser consultado.

    """
    try:
        with conexao.cursor() as cursor:
            sql = "SELECT nome, cpf, agencia, conta, endereco, data_nascimento FROM cliente WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente))
            registros = cursor.fetchall()

            if registros is not None:
                for registro in registros:
                    nome, cpf, agencia, conta, endereco, data_nascimento = registro
                    print(
                        f"INFO: {registro}"
                    )
            else:
                print("INFO: Nenhuma imagem encontrada com o ID especificado.")
    except Exception as e:
        print("INFO: Erro ao ler imagem do banco de dados.")
        print(f"ERROR: {e}")


#--------------------------------TABELA DOCUMENTO------------------------------------------
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
        with conexao.cursor() as cursor:
            cursor.execute(f'INSERT INTO Documento_Digital (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente))
            conexao.commit()
            cursor.close()
            print("INFO: Inserção realizada com sucesso.")
            return True
        
    except Exception as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

#--------------------------------TABELA USUARIO------------------------------------------
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
        with conexao.cursor() as cursor:
            cursor.execute(f'INSERT INTO Usuario (nome, cpf, user_name, senha) VALUES (%s, %s, %s, %s)', (nome, cpf, user_name, senha))
            conexao.commit()
            cursor.close()
            print('Dados inseridos na tabela USUARIO')
        
        return True
    except Exception as e:
        print("Erro ao inserir dados:", e)
        conexao.rollback()
        return False

#--------------------------------TABELA APLICACAO------------------------------------------
#inserir dados
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
        with conexao.cursor() as cursor:
            cursor.execute(f'INSERT INTO Aplicacao_Manipula (tipo_manipulacao, data_hora, id_usuario, id_documento) VALUES (%s, %s, %s, %s)', (tipo_manipulacao, data_hora, id_usuario, id_documento))
            conexao.commit()
            cursor.close()
            print('Dados inseridos na tabela USUARIO')
        
        return True
    except Exception as e:
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
    id_imagem = 2
    id_cliente = 2
    imagem = 'ImagensTeste/IMG_20240403_163932.jpg'

    
    #inserir_imagem(imagem, 'cedula01')
    # inserir_dados_cliente('Luis Carlos da Silva Bezerra', '002.754.533-40', '5555-5', '22222-0', 'Rua José Carneiro da Silva, n1234', '1985/11/26')
    #inserir_dados_documento(nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente)
    # inserir_dados_usuario('Fulano de Tal', '888.777.222-99', 'user01', 'abc123')
    inserir_dados_aplicacao('Inserção', '2023/12/15 15:55', 2, 3)
    #ler_imagem(1)
   
    #CONSULTAS
    #consultar_cliente_id('1')
'''
#------------------------------------------------ANTIGO---------------------------------------


#FUNÇÕES DE ATUALIZAÇÃO DO BANCO DE DADOS
#GENÉRICA:
#avaliar a escolha para atualição
def atualizar_dados_por_id(nome_tabela, id, **valores):
    # Construindo a parte SET da consulta SQL
    set_values = ', '.join([f"{coluna} = %s" for coluna in valores.keys()])
    
    # Construindo a consulta SQL completa
    consulta = f"UPDATE {nome_tabela} SET {set_values} WHERE id = %s"
    
    # Montando os valores a serem substituídos na consulta SQL
    valores_para_substituir = list(valores.values()) + [id]
    
    try:
        cursor = conexao.cursor()
        cursor.execute(consulta, valores_para_substituir)
        conexao.commit()
        print('Dados atualizados com sucesso!')
        return True
    
    except Exception as error:
        print(f'Falha ao atualizar os dados. Erro: {error}')
        conexao.rollback()
        return False
#------------------------------------------------------------------------------------------------------------------------------------------


 
'''