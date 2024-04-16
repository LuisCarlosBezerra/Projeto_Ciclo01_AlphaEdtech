import argon2

#CRIAR HASH
def encrypt_password(password):
    """
    Cria um Hash à partir de uma senha, utilizando o módulo argon2.
    O objetivo é que tenhamos o hash salvo no Banco de Dados, ao invés da senha.

    Argumentos:
        password (str): Senha que deveria ser salva no banco.

    Retornos:
        hashed_password (str): Hash da senha inserida na função.
    """     
    # Crie um objeto Argon2
    hasher = argon2.PasswordHasher()
    return hasher.hash(password)
 

#COMPARAR SENHA COM BANCO DE DADOS
def check_password(password, hashed_password):
    """
    Função para verificação da senha do usuário. É realizada a comparação da senha de entrada, com um hash salvo.
    Se ambos forem iguais haverá o retorno True, caso contrário False.

    Argumentos:
        hashed_password (str): Hash da senha que consta no banco de dados.

    Retornos:
        Boolen True or False
    """   
    # Crie um objeto Argon2
    hasher = argon2.PasswordHasher()
    try:
        # Verifique a senha
        hasher.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False


if __name__ == "__main__":
    #testando uma senha
    password = "senha123"
    crypted_pass = encrypt_password(password)
    print("Senha hash:", crypted_pass)

    # Verificar a senha
    if check_password("senha123", crypted_pass):
        print("Senha correta!")
    else:
        print("Senha incorreta!")