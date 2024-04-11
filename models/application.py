from datetime import datetime
from models.user import User
from models.digital_document import DigitalDocument


class Application:

    def __init__(
        self,
        manipulation_type: str,
        date_time: datetime,
        user: User,
        digital_document: DigitalDocument = None,
        id: int = None,
    ) -> None:
        self.id = id
        self.manipulation_type = manipulation_type
        self.date_time = date_time
        self.user = user
        self.digital_document = digital_document
