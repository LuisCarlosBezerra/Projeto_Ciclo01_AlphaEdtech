import psycopg2
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
        sql = f"SELECT user_name FROM Usuario WHERE user_name = '{user}'"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            if registros[0][0] == user:   
                consulta = cursor.execute(f"SELECT senha FROM Usuario WHERE user_name = '{user}'")
                pass_db = cursor.fetchone()
                try:
                    senha = check_password(input('Digite a sua senha cadastrada: '), pass_db[0])
                    print(senha)
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


