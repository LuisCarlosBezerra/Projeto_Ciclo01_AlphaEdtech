from datetime import date


class Client:
    """
    Represents a client entity.

    This class encapsulates information about a client, including their name, CPF,
    agency, account, address, and birth date.

    Attributes:
        id (int): The unique identifier of the client.
        name (str): The name of the client.
        cpf (str): The CPF (Cadastro de Pessoas Físicas) of the client.
        agency (str): The agency associated with the client.
        account (str): The account number associated with the client.
        address (str): The address of the client.
        birth_date (date): The birth date of the client.
    """

    def __init__(
        self,
        name: str,
        cpf: str,
        agency: str,
        account: str,
        address: str,
        birth_date: date,
        id: int = None,
    ) -> None:
        """
        Initializes a Client instance with the provided attributes.

        Args:
            name (str): The name of the client.
            cpf (str): The CPF (Cadastro de Pessoas Físicas) of the client.
            agency (str): The agency associated with the client.
            account (str): The account number associated with the client.
            address (str): The address of the client.
            birth_date (date): The birth date of the client.
            id (int, optional): The unique identifier of the client.
        """
        self.id = id
        self.name = name
        self.cpf = cpf
        self.agency = agency
        self.account = account
        self.address = address
        self.birth_date = birth_date

    def save_to_database(self, db):
        """
        Saves the client instance to the database.

        Args:
            db (DatabaseConnection): The database connection object.
        """

        insert_query = """
        INSERT INTO cliente (nome, cpf, agencia, conta, endereco, data_nascimento) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_cliente;
        """
        db.execute_query(
            insert_query,
            "Salvando Cliente",
            self.name,
            self.cpf,
            self.agency,
            self.account,
            self.address,
            self.birth_date,
        )
        self.id = db.cur.fetchone()[0]

    @staticmethod
    def from_database(db, client_id):
        """
        Retrieves a Client instance from the database based on the provided client ID.

        Args:
            db (DatabaseConnection): The database connection object.
            client_id (int): The ID of the client to retrieve.

        Returns:
            Client: The Client instance retrieved from the database.
        """
        select_query = """
        SELECT id_cliente, nome, cpf, agencia, conta, endereco, data_nascimento FROM cliente
        WHERE cliente.id_cliente = %s;
        """
        data = db.fetch_data(select_query, client_id)
        if data:
            (
                id,
                name,
                cpf,
                agency,
                account,
                address,
                birth_date,
            ) = data[0]

            return Client(
                id=id,
                name=name,
                cpf=cpf,
                agency=agency,
                account=account,
                address=address,
                birth_date=birth_date,
            )
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the Client instance.

        Returns:
            str: A string representation of the Client instance.
        """
        return f"Cliente = ( id = {self.id}, nome = {self.name}, cpf = {self.cpf}, agencia = {self.agency}, conta = {self.account}, endereco = {self.address}, nasciimento = {self.birth_date})"
