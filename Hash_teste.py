''' import psycopg2
from Hash_gen import encrypt_password, check_password
from user_DB import DB_NAME, USER, PASSWORD, HOST, PORT
from CRUD_db import inserir_dados_usuario

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


#simulando um login no sistema
#alimentando a senha e usuario no banco de dados
# senha_cadastrada = 'ABC123456'
# inserir_dados_usuario('Luis Carlos Bezerra', '111.888.321-01', 'LC99', encrypt_password(senha_cadastrada))


user = input('Digite o seu nome de usuário: ')
#consultar se o usuário existe no banco de dados
with conexao.cursor() as cursor:
    try:
        sql = f"SELECT user_name FROM Usuario WHERE user_name = %s"
        cursor.execute(sql, (user,))
        registros = cursor.fetchall()
        if registros:
            if registros[0][0] == user:   
                sql_pass = f"SELECT senha FROM Usuario WHERE user_name = %s"
                consulta = cursor.execute(sql_pass, (user,))
                pass_db = cursor.fetchone()
                try:
                    senha = check_password(input('Digite a sua senha cadastrada: '), pass_db[0])
                except Exception as error:
                    print(f'A função de verificação encontrou um problema. Talvez a senha salva no banco está em formato incorreto')
            else:
                print('Usuário não encontrado')

        else:
            print("Usuário não cadastrado ou username digitado incorretamente.")
    except Exception as e:
        print("INFO: Erro no banco de dados.")
        print(f"ERROR: {e}")


#input('Digite a sua senha: ')


'''
from models.user import User
from db.connection import DatabaseConnection
from models.image import ImageClass
from PIL import Image
from models.client import Client
from models.digital_document import DigitalDocument

#objeto conexão
banco_conect = DatabaseConnection("postgres","Siulsolrac32","provaPython","localhost",5432)
#objeto usuário
usuario = User('Luis Carlos Bezerra', '001.001.002-00', 'SOLRAC', '123456')
#usuario.save_to_database(banco_conect)
#objeto imagem
imagem = ImageClass('documento 02', image_path='images\print_livro.png')
#imagem.save_to_database(banco_conect)
#imagem.show_image()
#criando um objeto cliente
cliente = Client('Sebastiao Nunes Maia', '985.900.001-34', '33545', '87921-2', 'Rua Candido Nunes, bairro Juremal','25/12/1988')
#cliente.save_to_database(banco_conect)
#criando um objeto documento
documento = DigitalDocument('Carlos do Nascimento Filho', 'AR25GA06', '30/12/2022', 3854.85, '58-21456-12', imagem, cliente)
documento.save_to_database(banco_conect)



