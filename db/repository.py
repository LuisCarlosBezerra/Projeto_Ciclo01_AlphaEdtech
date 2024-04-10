import psycopg2 as p
from db.connection import DatabaseConnection
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt


class DatabaseQueries:
    """
    Class to execute queries in PostgreSQL database.
    """

    def __init__(self, connection):
        """
        Initializes the class with the database connection object.

        Args:
            connection (connection): Database connection object.
        """
        self.connection = connection

    def insert_image(self, image_path, image_name):
        """
        Inserts an image into the database.

        Args:
            image_path (str): Path of the image file.
            image_name (str): Name of the image.

        Returns:
            bool: True if insertion is successful, False otherwise.
        """
        try:
            with self.connection.cursor() as cursor:
                with open(image_path, "rb") as image_file:
                    img = image_file.read()

                    cursor.execute(
                        f"""
                        INSERT INTO imagens (nome_imagem, imagem) 
                            VALUES ('{image_name}', {p.Binary(img)});
                        """
                    )

                print("INFO: Inserção realizada com sucesso.")
                self.connection.commit()
                return True
        except Exception as e:
            print("INFO: Erro ao inserir imagem no banco de dados.")
            print(f"ERROR: {e}")
            self.connection.rollback()
            return False

    def read_image(self, image_id):
        """
        Reads an image from the database and displays it.

        Args:
            image_id (int): ID of the image to be read.

        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT nome_imagem, imagem FROM imagens WHERE id_imagem = %s"
                cursor.execute(sql, (image_id,))
                registro = cursor.fetchone()

                if registro is not None:
                    nome_imagem, dados_imagem = registro
                    imagem_stream = BytesIO(dados_imagem)
                    imagem = Image.open(imagem_stream)
                    nome_arquivo_saida = f"imagem_recuperada_{image_id}.jpg"
                    plt.imshow(imagem)
                    plt.show()
                    print(
                        f"INFO: Imagem {nome_imagem} recuperada e salva como {nome_arquivo_saida}"
                    )
                else:
                    print("INFO: Nenhuma imagem encontrada com o ID especificado.")
        except Exception as e:
            print("INFO: Erro ao ler imagem do banco de dados.")
            print(f"ERROR: {e}")


# Example usage of the classes
if __name__ == "__main__":
    try:
        db_connection = DatabaseConnection(
            user="postgres",
            password="12345",
            host="localhost",
            dbname="sistema_banco_ocr",
        )
        connection = db_connection.connect()

        db_queries = DatabaseQueries(connection)
        result = db_queries.insert_image(
            image_path="C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/Projeto_Ciclo01_AlphaEdtech/imagens-teste/cedula-banco-daycoval-menor.png",
            image_name="imagem.jpg",
        )

        if result:
            print("INFO: Imagem inserida com sucesso!")
        else:
            print("INFO: Falha ao inserir imagem.")
    finally:
        if connection:
            db_connection.disconnect(connection)
