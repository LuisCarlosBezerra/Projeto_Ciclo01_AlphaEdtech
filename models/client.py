from datetime import date


class Client:

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
        self.id = id
        self.name = name
        self.cpf = cpf
        self.agency = agency
        self.account = account
        self.address = address
        self.birth_date = birth_date

    def save_to_database(self, db):
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
        return f"Cliente = ( id = {self.id}, nome = {self.name}, cpf = {self.cpf}, agencia = {self.agency}, conta = {self.account}, endereco = {self.address}, nasciimento = {self.birth_date})"
