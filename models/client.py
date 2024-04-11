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
