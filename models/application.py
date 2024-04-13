from datetime import datetime
from models.user import User
from models.digital_document import DigitalDocument
from models.image import ImageClass
from models.client import Client
from datetime import datetime


class Application:
    """
    Represents an application manipulation entity.

    This class encapsulates information about an application manipulation, including its type,
    date and time, user, and associated digital document.

    Attributes:
        id (int): The unique identifier of the application manipulation.
        manipulation_type (str): The type of manipulation performed in the application.
        date_time (datetime): The date and time when the application was performed.
        user (User): The user who performed the application manipulation.
        digital_document (DigitalDocument): The digital document associated with the application.
    """

    def __init__(
        self,
        manipulation_type: str,
        date_time: datetime,
        user: User,
        digital_document: DigitalDocument = None,
        id: int = None,
    ) -> None:
        """
        Initializes an Application instance with the provided attributes.

        Args:
            manipulation_type (str): The type of manipulation performed in the application.
            date_time (datetime): The date and time when the application was performed.
            user (User): The user who performed the application manipulation.
            digital_document (DigitalDocument, optional): The digital document associated with the application.
            id (int, optional): The unique identifier of the application manipulation.
        """
        self.id = id
        self.manipulation_type = manipulation_type
        self.date_time = date_time
        self.user = user
        self.digital_document = digital_document

    def save_to_database(self, db):
        """
        Saves the application manipulation instance to the database.

        Args:
            db (DatabaseConnection): The database connection object.
        """
        self.user.save_to_database(db)
        self.digital_document.save_to_database(db)
        insert_query = """
        INSERT INTO aplicacao_manipula (tipo_manipulacao, data_hora, id_usuario, id_documento) 
            VALUES (%s, %s, %s, %s) RETURNING id_man;
        """
        db.execute_query(
            insert_query,
            "Salvando Aplicacao",
            self.manipulation_type,
            self.date_time,
            self.user.id,
            self.digital_document.id,
        )
        self.id = db.cur.fetchone()[0]

    @staticmethod
    def from_database(db, application_id):
        """
        Retrieves an Application instance from the database based on the provided application ID.

        Args:
            db (DatabaseConnection): The database connection object.
            application_id (int): The ID of the application manipulation to retrieve.

        Returns:
            Application: The Application instance retrieved from the database.
        """
        select_query = """
        SELECT a.id_man, a.tipo_manipulacao, a.data_hora, d.id_documento, 
        d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, d.id_imagem, d.id_cliente,
		u.id_usuario, u.nome, u.cpf, u.user_name, u.senha
		FROM aplicacao_manipula a
        LEFT JOIN documento_digital d ON a.id_documento = d.id_documento
        LEFT JOIN usuario u ON a.id_usuario = u.id_usuario
        WHERE a.id_man = %s;
        """
        data = db.fetch_data(select_query, application_id)
        if data:
            (
                id_aplicacao,
                manipulation_type,
                date_time,
                id_document,
                agent_name,
                physical_location,
                contract_date,
                credit_value,
                certificate_number,
                id_image,
                id_client,
                id_user,
                name_user,
                cpf_user,
                user_name,
                password,
            ) = data[0]

            return Application(
                id=id_aplicacao,
                manipulation_type=manipulation_type,
                date_time=date_time,
                digital_document=DigitalDocument(
                    id=id_document,
                    agent_name=agent_name,
                    physical_location=physical_location,
                    contract_date=contract_date,
                    credit_value=credit_value,
                    certificate_number=certificate_number,
                    image=ImageClass.from_database(db, id_image),
                    client=Client.from_database(db, id_client),
                ),
                user=User(
                    id=id_user,
                    name=name_user,
                    cpf=cpf_user,
                    user_name=user_name,
                    password=password,
                ),
            )
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the Application instance.

        Returns:
            str: A string representation of the Application instance.
        """
        return f"Aplicação = ( id = {self.id}, tipo de manipulação = {self.manipulation_type}, Data e hora = {self.date_time}, Usuario = {self.user}, Documento = {self.digital_document})"
