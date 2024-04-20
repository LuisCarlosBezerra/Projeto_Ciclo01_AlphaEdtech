import argon2
import secrets


class PasswordManager:
    def __init__(self):
        """
        Inicializa o gerenciador de senhas com um objeto hasher do Argon2.
        """
        self.hasher = argon2.PasswordHasher()

    def encrypt_password(self, password):
        """
        Gera um hash para a senha fornecida, adicionando um salt aleatório.

        Argumentos:
            password (str): A senha a ser hashada.

        Retornos:
            str: O hash da senha combinada com salt, formatado como 'hash:salt'.
        """
        salt = secrets.token_hex(16)  # Gera 16 bytes de salt
        salted_password = password + salt
        hash_pass = self.hasher.hash(salted_password)
        return hash_pass + ":" + salt

    def check_password(self, password, hashed_password):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.

        Argumentos:
            password (str): A senha a ser verificada.
            hashed_password (str): O hash armazenado, incluindo o salt.

        Retornos:
            bool: True se a senha corresponder ao hash, False caso contrário.
        """
        stored_hash, salt = hashed_password.split(":")
        salted_password = password + salt
        try:
            self.hasher.verify(stored_hash, salted_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False


# Demonstração de uso da classe
if __name__ == "__main__":
    password_manager = PasswordManager()
    user_password = "senha5"
    encrypted_password = password_manager.encrypt_password(user_password)
    print(f"Senha hash: {encrypted_password}")

    # Verificando a senha com o hash gerado
    if password_manager.check_password("senha5", encrypted_password):
        print("Senha correta!")
    else:
        print("Senha incorreta!")
