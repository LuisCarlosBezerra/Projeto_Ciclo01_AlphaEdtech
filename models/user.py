class User:
    """
    Represents a user entity.

    This class encapsulates information about a user, including their name, CPF,
    username, and password.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        cpf (str): The CPF (Cadastro de Pessoas Físicas) of the user.
        user_name (str): The username of the user.
        password (str): The password of the user.
    """

    def __init__(
        self,
        name: str,
        cpf: str,
        user_name: str,
        password: str,
        id: int = None,
    ) -> None:
        """
        Initializes a User instance with the provided attributes.

        Args:
            name (str): The name of the user.
            cpf (str): The CPF (Cadastro de Pessoas Físicas) of the user.
            user_name (str): The username of the user.
            password (str): The password of the user.
            id (int, optional): The unique identifier of the user.
        """
        self.id = id
        self.name = name
        self.cpf = cpf
        self.user_name = user_name
        self.password = password

    def save_to_database(self, db):
        """
        Saves the user instance to the database.

        Args:
            db (DatabaseConnection): The database connection object.
        """
        insert_query = """
        INSERT INTO usuario (nome, cpf, user_name, senha) 
            VALUES (%s, %s, %s, %s) RETURNING id_usuario;
        """
        db.execute_query(
            insert_query,
            "Salvando Usuario",
            self.name,
            self.cpf,
            self.user_name,
            self.password,
        )
        self.id = db.cur.fetchone()[0]

    @staticmethod
    def from_database(db, client_id):
        """
        Retrieves a User instance from the database based on the provided user ID.

        Args:
            db (DatabaseConnection): The database connection object.
            client_id (int): The ID of the user to retrieve.

        Returns:
            User: The User instance retrieved from the database.
        """
        select_query = """
        SELECT id_usuario, nome, cpf, user_name, senha FROM usuario
        WHERE usuario.id_usuario = %s;
        """
        data = db.fetch_data(select_query, client_id)
        if data:
            (
                id,
                name,
                cpf,
                user_name,
                password,
            ) = data[0]

            return User(
                id=id,
                name=name,
                cpf=cpf,
                user_name=user_name,
                password=password,
            )
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance.
        """
        return f"Usuario = ( id = {self.id}, nome = {self.name}, cpf = {self.cpf}, user_name = {self.user_name}, senha = {self.password})"
