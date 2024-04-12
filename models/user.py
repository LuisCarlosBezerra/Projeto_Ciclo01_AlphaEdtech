class User:

    def __init__(
        self,
        name: str,
        cpf: str,
        user_name: str,
        password: str,
        id: int = None,
    ) -> None:
        self.id = id
        self.name = name
        self.cpf = cpf
        self.user_name = user_name
        self.password = password

    def save_to_database(self, db):
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
        return f"Usuario = ( id = {self.id}, nome = {self.name}, cpf = {self.cpf}, user_name = {self.user_name}, senha = {self.password})"
