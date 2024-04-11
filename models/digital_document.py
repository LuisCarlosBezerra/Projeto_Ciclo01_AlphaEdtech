from datetime import date
from models.image import Image
from models.client import Client


class DigitalDocument:

    def __init__(
        self,
        agent_name: str,
        physical_location: str,
        contract_date: date,
        credit_value: float,
        certificate_number: int,
        image: Image,
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
