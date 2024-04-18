import argon2   #módulo para implementar hash na senha
import secrets  #módulo para acrescentar um "salt" à senha (série de caracteres adicionais)


#Criar HASH da senha + salt
def encrypt_password(password):
    """
    A função recebe a senha e a combina com uma sequência extra de caracters, formando 
    uma nova string, conhecida como "salted". À artir dessa combinação, e utilizando o 
    módulo argon2, geramos um hash mais forte do que se tivessemos apenas criado o hash
    da senha original. 

    Argumentos:
        password (str): Senha que deve ser salva no banco.
        salt (str): Sequência de caracteres gerada pelo módulo secrets, para ser acrescido
        à senha original, oferecendo uma camada extra de proteção contra ataques de dicionário
        ou força bruta.
        salted_password (str): Combinação entre a password e o salt, descritos acima.
        hasher (Argon2): Objeto gerado à partir do módulo Argon2, que irá criar o nosso hash
        hash_pass (str): Hash gerado à partir do método hash() do objeto hasher.

    Retornos:
        hash_pass + ':' + salt (str): A saída é uma combinação do hash gerado pela 
        string salted_password(combinação entre senha + salt), e o próprio salt gerado
        inicialmente. O caractere ':' é utilizado entre as strings para podermos separamos
        adiante e verificar a veracidade da senha na função check_password.
    """     
    salt = secrets.token_hex(16)  # 16 bytes (128 bits) de salt
    #Combinando a senha + salt em uma única string
    salted_password = password + salt
    #Criando um objeto Argon2, utilizado para criar o nosso hash
    hasher = argon2.PasswordHasher()
    #Criando um hash para a salted_password
    hash_pass = hasher.hash(salted_password)
    return hash_pass + ':' + salt
 

#COMPARAR SENHA COM BANCO DE DADOS
def check_password(password, hashed_password):
    """
    Função para verificação da senha do usuário. Ela recebe como parâmetros a password
    do usuário e a sequencia de caracteres gravada no banco. É realizada uma separação
    na string que está no banco, para obtermos o hash e o salt. À partir daí conseguimos, 
    combinar a senha com o salt (processo parecido com o da função encrypt_password) e 
    comparar com o hash, verificando assim sua validade ou não.

    Argumentos:
        password (str): Senha digitada pelo usuário, à ser validada ou não.
        hashed_password (str): Hash da senha que consta no banco de dados.
        stored_hash (str): Parte separada da string que está salva no banco, referindo-se
        apenas ao hash gerado da combinação da password com o salt.
        salt (str): Sequência de caracteres combinados com a senha para gerar o hash. Aqui
        será utilizada para ser combinada com a password para verificar a validade da senha.

    Retornos:
        Boolean True or False, dependendo do resultado da função verify(stored_hash, salted_password)m
        que verifica se a senha é igual ao hash que está no banco de dados.
    """   
    #separando a string salva no banco (hash:salt), obtendo o hash e o salt separados.
    stored_hash, salt = hashed_password.split(':')
    #Acrescentando o salt à password de entrada (padrão que foi gerado o hash do banco)
    salted_password = password + salt
    #Criando um objeto Argon2, utilizado para comparar o hash com a salted_password (password + salt)
    hasher = argon2.PasswordHasher()
    try:
        #Verificação da senha
        hasher.verify(stored_hash, salted_password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False


if __name__ == "__main__":
    #Senha para futura verificação.
    password = "senha5"
    #Chamando a função de criação do hash da senha.
    crypted_pass = encrypt_password(password)
    #Mostrando a string gerada (hash:salt)
    print(f"Senha hash: {crypted_pass}")
 
    #Verificando a senha com o hash gerado à partir da senha original.
    if check_password("senha5", crypted_pass):
        print("Senha correta!")
    else:
        print("Senha incorreta!")