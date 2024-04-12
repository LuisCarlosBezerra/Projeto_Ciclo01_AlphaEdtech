from datetime import date
from models.image import ImageClass
from models.client import Client


class DigitalDocument:

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
        self.id = id
        self.agent_name = agent_name
        self.physical_location = physical_location
        self.contract_date = contract_date
        self.credit_value = credit_value
        self.certificate_number = certificate_number
        self.image = image
        self.client = client

    def save_to_database(self, db):
        self.image.save_to_database(db)
        self.client.save_to_database(db)
        insert_query = """
        INSERT INTO documento_digital (nome_agente, localizacao_fisica, data_contrato, valor_credito, numero_cedula, id_imagem, id_cliente) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_documento;
        """
        db.execute_query(
            insert_query,
            "Salvando Cliente",
            self.agent_name,
            self.physical_location,
            self.contract_date,
            self.credit_value,
            self.certificate_number,
            self.image.id,
            self.client.id,
        )
        self.id = db.cur.fetchone()[0]

    @staticmethod
    def from_database(db, document_id):
        select_query = """
        SELECT d.id_documento, d.nome_agente, d.localizacao_fisica, d.data_contrato,  d.valor_credito,
		d.numero_cedula, i.id_imagem, i.nome_imagem, i.imagem, ci.id_cliente, 
		ci.nome, ci.cpf, ci.agencia, ci.conta, ci.endereco, ci.data_nascimento 
		FROM documento_digital d
        LEFT JOIN cliente ci ON d.id_cliente = ci.id_cliente
        LEFT JOIN imagens i ON d.id_imagem = i.id_imagem
        WHERE d.id_documento = %s;
        """
        data = db.fetch_data(select_query, document_id)
        print(data)
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

    def __str__(self) -> str:
        return f"Documento Digital = ( id = {self.id}, nome_agente = {self.agent_name}, localizacao_fisica = {self.physical_location}, data_contrato = {self.contract_date}, valor_credito = {self.credit_value}, numero_cedula = {self.certificate_number}, id_imagem = {self.image}, id_cliente = {self.client})"
