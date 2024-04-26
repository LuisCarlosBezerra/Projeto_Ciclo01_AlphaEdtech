from interfaces.CLASSES_TELAS.classe_tela_login import TelaLogin
from models.user import User
from user_DB import DB_NAME, USER, PASSWORD
from db.repository import Repository

"""
Este arquivo contém o código principal para a execução da aplicação. Ele importa classes e módulos necessários para o 
funcionamento do sistema, como a interface de tela de login, modelos de usuário, documentos digitais, inscrições, 
além de outras dependências como data e hora, configurações de banco de dados e o repositório de dados.

O código é encapsulado em um bloco `try` para lidar com exceções que possam ocorrer durante a execução. 
Ele tenta inicializar uma conexão com o banco de dados e instanciar objetos de usuário. 
Se houver sucesso, tenta realizar o login de um usuário específico e iniciar a interface de tela de login.

Se ocorrer uma exceção, o bloco `finally` garante que a conexão com o banco de dados seja fechada adequadamente.

Este código é parte integrante de um projeto maior e serve como ponto de entrada para a aplicação.
"""
try:
    """
    O repostiório necessita do USER, PASSWORD E DB_NAME do seu banco de dados já criado no postgres.
    """
    repository = Repository(user=USER, password=PASSWORD, dbname=DB_NAME)
    # db = repository.db
    """
    É necessário ter usuários cadastrados no sistema:
        carlos_pereira = User("CP", "829088040-50", "CP", "12345")
        #repository.register(carlos_pereira)
        print(repository.login("CP", "12345"))
        print(repository.user)

    Os campos usados como argumentos na instância da classe User são respectivamente:
    Nome do usuário;
    CPF do usuário;
    Use_name do usuário para logar no sistema;
    Senha do usuário para logar no sistema
    """

    app = TelaLogin(repository)
    app.run()

finally:
    pass
