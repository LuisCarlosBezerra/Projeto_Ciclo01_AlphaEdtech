from PIL import Image


class ImageClass:
    def __init__(
        self,
        image_name: str,
        image_data: Image,
        id: int = None,
    ) -> None:
        self.id = id
        self.image_name = image_name
        self.image_data = image_data
