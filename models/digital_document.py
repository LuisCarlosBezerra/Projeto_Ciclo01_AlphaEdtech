from datetime import date
from models.image import ImageClass
from models.client import Client


class DigitalDocument:
    """
    Represents a digital document entity.

    This class encapsulates information about a digital document, including the agent name,
    physical location, contract date, credit value, certificate number, associated image,
    and client.

    Attributes:
        id (int): The unique identifier of the digital document.
        agent_name (str): The name of the agent associated with the digital document.
        physical_location (str): The physical location of the digital document.
        contract_date (date): The contract date of the digital document.
        credit_value (float): The credit value of the digital document.
        certificate_number (int): The certificate number of the digital document.
        image (ImageClass): The image associated with the digital document.
        client (Client): The client associated with the digital document.
    """

    def __init__(
        self,
        agent_name: str,
        physical_location: str,
        contract_date: date,
        credit_value: float,
        certificate_number: int,
        image: ImageClass,
        client: Client,
        id: int = None,
    ) -> None:
        """
        Initializes a DigitalDocument instance with the provided attributes.

        Args:
            agent_name (str): The name of the agent associated with the digital document.
            physical_location (str): The physical location of the digital document.
            contract_date (date): The contract date of the digital document.
            credit_value (float): The credit value of the digital document.
            certificate_number (int): The certificate number of the digital document.
            image (ImageClass): The image associated with the digital document.
            client (Client): The client associated with the digital document.
            id (int, optional): The unique identifier of the digital document.
        """
        self.id = id
        self.agent_name = agent_name
        self.physical_location = physical_location
        self.contract_date = contract_date
        self.credit_value = credit_value
        self.certificate_number = certificate_number
        self.image = image
        self.client = client

    def save_to_database(self, db):
        """
        Saves the digital document instance to the database.

        Args:
            db (DatabaseConnection): The database connection object.
        """
        self.image.save_to_database(db)
        self.client.save_to_database(db)
        insert_query = """
        INSERT INTO documento_digital (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_documento;
        """
        db.execute_query(
            insert_query,
            "Salvando Documento",
            self.agent_name,
            self.physical_location,
            self.contract_date,
            self.credit_value,
            self.certificate_number,
            self.image.id,
            self.client.id,
        )
        try:
            self.id = db.cur.fetchone()[0]
        except Exception as error:
            print(
                f"Dados não salvos no banco. Chaves únicas já existem no banco. Erro: {error}"
            )

    @staticmethod
    def from_database(db, document_id):
        """
        Retrieves a DigitalDocument instance from the database based on the provided document ID.

        Args:
            db (DatabaseConnection): The database connection object.
            document_id (int): The ID of the digital document to retrieve.

        Returns:
            DigitalDocument: The DigitalDocument instance retrieved from the database.
        """
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagem i ON d.id_imagem = i.id_imagem
        WHERE d.id_documento = %s;
        """
        data = db.fetch_data(select_query, document_id)
        if data:
            (
                id_document,
                agent_name,
                physical_location,
                contract_date,
                credit_value,
                certificate_number,
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
            ) = data[0]

            return DigitalDocument(
                id=id_document,
                agent_name=agent_name,
                physical_location=physical_location,
                contract_date=contract_date,
                credit_value=credit_value,
                certificate_number=certificate_number,
                image=ImageClass(id=id_image, image_data=image, image_name=image_name),
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
        else:
            return None

    @staticmethod
    def array_from_db_by_certificate_number(
        db, certificate_number
    ) -> list["DigitalDocument"]:
        """
        Retrieves an array of DigitalDocument instances from the database based on the provided certificate number.

        Args:
            db (DatabaseConnection): The database connection object.
            certificate_number (str): The certificate number or a portion of it to search for.

        Returns:
            List[DigitalDocument] or None: An array of DigitalDocument instances retrieved from the database
                that match the provided certificate number. Returns None if no matching documents are found.
        """
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagem i ON d.id_imagem = i.id_imagem
        WHERE d.numero_cedula LIKE %s;
        """
        data = db.fetch_data(select_query, f"%{certificate_number}%")
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
                documents.append(
                    DigitalDocument(
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

    @staticmethod
    def from_db_by_certificate_number(db, certificate_number) -> "DigitalDocument":
        """
        Retrieves a DigitalDocument instance from the database based on the provided certificate number.

        Args:
            db (DatabaseConnection): The database connection object.
            certificate_number (str): The certificate number to search for.

        Returns:
            DigitalDocument or None: The DigitalDocument instance retrieved from the database
                that matches the provided certificate number. Returns None if no matching document is found.
        """
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagem i ON d.id_imagem = i.id_imagem
        WHERE d.numero_cedula = %s;
        """
        data = db.fetch_data(select_query, certificate_number)
        if data:
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
            ) = data[0]

            return DigitalDocument(
                id=id_document,
                agent_name=agent_name,
                physical_location=physical_location,
                contract_date=contract_date,
                credit_value=credit_value,
                certificate_number=c_number,
                image=ImageClass(id=id_image, image_data=image, image_name=image_name),
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
        else:
            return None

    @staticmethod
    def from_db_by_choice(
        db,
        ct_date_init=None,
        ct_date_last=None,
        ag_name=None,
        cr_value_init=None,
        cr_value_last=None,
        cl_name=None,
    ) -> list["DigitalDocument"]:
        """
        Retrieves DigitalDocument instances from the database based on the provided criteria.

        Args:
            db (DatabaseConnection): The database connection object.
            ct_date_init (str): The initial contract date to search for.
            ct_date_last (str): The last contract date to search for.
            ag_name (str): The agent name to search for.
            cr_value_init (float): The initial credit value to search for.
            cr_value_last (float): The last credit value to search for.
            cl_name (str): The client name to search for.

        Returns:
            List[DigitalDocument] or None: A list of DigitalDocument instances retrieved from the database
                based on the provided criteria. Returns None if no matching documents are found.
        """
        if (
            cl_name
            and ag_name is None
            and ct_date_init is None
            and ct_date_last is None
            and cr_value_init is None
            and cr_value_last is None
        ):
            return Client.documents_from_db_by_name(
                db, cl_name=cl_name, class_document=DigitalDocument
            )
        values = ()
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagem i ON d.id_imagem = i.id_imagem
        WHERE"""
        print(len(select_query))
        if ag_name:
            values = values + (f"%{ag_name}%",)
            select_query += " LOWER(d.nome_agente) LIKE LOWER(%s)"
        if cr_value_init:
            values = values + (cr_value_init, cr_value_last)
            if len(select_query) == 408:
                select_query += " d.valor_credito BETWEEN %s AND %s"
            else:
                select_query += " AND d.valor_credito BETWEEN %s AND %s"
        if ct_date_init:
            values = values + (ct_date_init, ct_date_last)
            if len(select_query) == 408:
                select_query += " d.data_contrato BETWEEN %s AND %s"
            else:
                select_query += " AND d.data_contrato BETWEEN %s AND %s"
        select_query += ";"

        data = db.fetch_data(select_query, *values)
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
                if cl_name:
                    if cl_name.lower() in client_name.lower():
                        documents.append(
                            DigitalDocument(
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
                else:
                    documents.append(
                        DigitalDocument(
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

    def from_db_order_by(
        db,
        cl_name=True,
        ag_name=False,
        c_number=False,
        cont_date=False,
        cr_value=False,
        asc=True,
    ):
        """
        Executes a database query to return a list of digital documents sorted
        based on criteria specified by the parameters.

        Parameters:
            db (DatabaseConnection): An instance of the database connection.
            cl_name (bool): Sort by client name (default True).
            ag_name (bool): Sort by agent name.
            c_number (bool): Sort by certificate number.
            cont_date (bool): Sort by contract date.
            cr_value (bool): Sort by credit value.
            asc (bool): Sort in ascending order (default True), False for descending.

        Returns:
            list: A list of `DigitalDocument` instances representing the retrieved documents, or
            None if no information is found.

        Exceptions:
            May raise exceptions related to connection failures or query execution errors in the database.
        """

        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagem i ON d.id_imagem = i.id_imagem
        """

        if ag_name == True or c_number == True or cont_date == True or cr_value == True:
            cl_name = False

        if cl_name == True:
            if asc == True:
                select_query += " ORDER BY ci.nome ASC;"
            else:
                select_query += " ORDER BY ci.nome DESC;"
        elif ag_name == True:
            if asc == True:
                select_query += " ORDER BY d.nome_agente ASC;"
            else:
                select_query += " ORDER BY d.nome_agente DESC;"
        elif c_number == True:
            if asc == True:
                select_query += " ORDER BY d.numero_cedula ASC;"
            else:
                select_query += " ORDER BY d.numero_cedula DESC;"
        elif cont_date == True:
            if asc == True:
                select_query += " ORDER BY d.data_contrato ASC;"
            else:
                select_query += " ORDER BY d.data_contrato DESC;"
        elif cr_value == True:
            if asc == True:
                select_query += " ORDER BY d.valor_credito ASC;"
            else:
                select_query += " ORDER BY d.valor_credito DESC;"
        data = db.fetch_data(select_query)
        documents = []
        if data:
            for d in data:

                (
                    id_document,
                    agent_name,
                    physical_location,
                    contract_date,
                    credit_value,
                    certificate_number,
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
                documents.append(
                    DigitalDocument(
                        id=id_document,
                        agent_name=agent_name,
                        physical_location=physical_location,
                        contract_date=contract_date,
                        credit_value=credit_value,
                        certificate_number=certificate_number,
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
        Returns a string representation of the DigitalDocument instance.

        Returns:
            str: A string representation of the DigitalDocument instance.
        """
        return f"Documento Digital = ( id = {self.id}, nome_agente = {self.agent_name}, localizacao_fisica = {self.physical_location}, data_contrato = {self.contract_date}, valor_credito = {self.credit_value}, numero_cedula = {self.certificate_number}, imagem = {self.image}, cliente = {self.client})"
