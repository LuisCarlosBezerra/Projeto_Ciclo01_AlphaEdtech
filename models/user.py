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
