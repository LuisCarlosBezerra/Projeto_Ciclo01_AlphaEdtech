from PIL import Image
import psycopg2 as p
from io import BytesIO
import matplotlib.pyplot as plt


class ImageClass:
    """
    Represents an image entity.

    This class encapsulates information about an image, including its name, data, and path.

    Attributes:
        id (int): The unique identifier of the image.
        image_name (str): The name of the image.
        image_data (Image): The image data (PIL Image object).
        image_path (str): The path to the image file.
    """

    def __init__(
        self,
        image_name: str,
        image_data: Image = None,
        image_path: str = None,
        id: int = None,
    ) -> None:
        """
        Initializes an ImageClass instance with the provided attributes.

        Args:
            image_name (str): The name of the image.
            image_data (Image, optional): The image data (PIL Image object).
            image_path (str, optional): The path to the image file.
            id (int, optional): The unique identifier of the image.
        """
        self.id = id
        self.image_name = image_name
        self.image_data = image_data
        self.image_path = image_path
        if image_path:
            try:
                self.image_data = Image.open(image_path)
                print("INFO: Imagem lida com sucesso!")
            except Exception as e:
                print("INFO: Imagem não reconhecida!")
                raise e
        if image_data:
            imagem_stream = BytesIO(image_data)
            self.image_data = Image.open(imagem_stream)

    def save_to_database(self, db):
        """
        Saves the image instance to the database.

        Args:
            db (DatabaseConnection): The database connection object.
        """
        insert_query = """
        INSERT INTO imagem (nome_imagem, imagem) VALUES (%s, %s) RETURNING id_imagem;
        """
        img_file = open(self.image_path, "rb")
        img = img_file.read()
        db.execute_query(
            insert_query, "Salvando Imagem", self.image_name, p.Binary(img)
        )
        img_file.close()
        self.id = db.cur.fetchone()[0]

    @staticmethod
    def from_database(db, image_id):
        """
        Retrieves an ImageClass instance from the database based on the provided image ID.

        Args:
            db (DatabaseConnection): The database connection object.
            image_id (int): The ID of the image to retrieve.

        Returns:
            ImageClass: The ImageClass instance retrieved from the database.
        """
        select_query = """
        SELECT id_imagem, nome_imagem, imagem FROM imagens
        WHERE imagem.id_imagem = %s;
        """
        data = db.fetch_data(select_query, image_id)
        if data:
            (
                id_image,
                image_name,
                image,
            ) = data[0]

            return ImageClass(image_name, id=id_image, image_data=image)
        else:
            return None

    def show_image(self):
        """
        Displays the image using Matplotlib.

        This method displays the image using Matplotlib's imshow function.

        """
        if self.image_data is not None:

            self.image_data.show()
            print("INFO: Imagem mostrada com sucesso!")
        else:
            print("INFO: Imagem mostrada sem sucesso!")

    def __str__(self) -> str:
        """
        Returns a string representation of the ImageClass instance.

        Returns:
            str: A string representation of the ImageClass instance.
        """
        return f"Imagem = ( id = {self.id}, nome da Imagem = {self.image_name})"
