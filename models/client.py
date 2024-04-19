from datetime import date

# from models.digital_document import DigitalDocument
from models.image import ImageClass


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
        try:
            self.id = db.cur.fetchone()[0]
        except Exception as error:
            print(f'Dados não salvos no banco. Chaves únicas já existem no banco. Erro: {error}')

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

    @staticmethod
    def documents_from_db_by_name(db, cl_name, class_document):
        """
        Retrieves a list of document instances associated with a client name from the database.

        Args:
            db (DatabaseConnection): The database connection object.
            cl_name (str): The name of the client or a portion of it to search for.
            class_document (class): The class of the document instances to be retrieved.

        Returns:
            List[Document] or None: A list of document instances retrieved from the database
                that match the provided client name. Returns None if no matching documents are found.
        """
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
                d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente,
                ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento
                FROM cliente ci
        LEFT JOIN documento_digital d ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagens i ON d.id_imagem = i.id_imagem
        WHERE LOWER(ci.nome) LIKE LOWER(%s);
        """

        data = db.fetch_data(select_query, f"%{cl_name}%")
        documents = []
        if data:
            for d in data:

                (
                    id_document,
                    agent_name,
                    physical_location,
                    contract_date,
                    credit_value,
                    c_number,
                    id_image,
                    image_name,
                    image,
                    id_client,
                    client_name,
                    cpf,
                    agency,
                    account,
                    address,
                    birth_date,
                ) = d
                if cl_name.lower() in client_name.lower():
                    documents.append(
                        class_document(
                            id=id_document,
                            agent_name=agent_name,
                            physical_location=physical_location,
                            contract_date=contract_date,
                            credit_value=credit_value,
                            certificate_number=c_number,
                            image=ImageClass(
                                id=id_image, image_data=image, image_name=image_name
                            ),
                            client=Client(
                                id=id_client,
                                name=client_name,
                                cpf=cpf,
                                agency=agency,
                                account=account,
                                address=address,
                                birth_date=birth_date,
                            ),
                        )
                    )

            return documents
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the Client instance.

        Returns:
            str: A string representation of the Client instance.
        """
        return f"Cliente = ( id = {self.id}, nome = {self.name}, cpf = {self.cpf}, agencia = {self.agency}, conta = {self.account}, endereco = {self.address}, nasciimento = {self.birth_date})"
