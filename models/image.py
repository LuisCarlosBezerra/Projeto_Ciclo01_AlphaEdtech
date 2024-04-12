from PIL import Image
import psycopg2 as p
from io import BytesIO
import matplotlib.pyplot as plt


class ImageClass:
    def __init__(
        self,
        image_name: str,
        image_data: Image = None,
        image_path: str = None,
        id: int = None,
    ) -> None:
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
        insert_query = """
        INSERT INTO imagens (nome_imagem, imagem) VALUES (%s, %s) RETURNING id_imagem;
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
        select_query = """
        SELECT id_imagem, nome_imagem, imagem FROM imagens
        WHERE imagens.id_imagem = %s;
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
        if self.image_data is not None:
            plt.imshow(self.image_data)
            plt.show()
            print("INFO: Imagem mostrada com sucesso!")
        else:
            print("INFO: Imagem mostrada sem sucesso!")
