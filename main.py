from db.connection import DatabaseConnection
from db.repository import DatabaseQueries
from models.image import ImageClass
from models.client import Client
from models.user import User
from models.digital_document import DigitalDocument
from datetime import date


if __name__ == "__main__":
    try:
        db_connection = DatabaseConnection(
            user="postgres",
            password="12345",
            host="localhost",
            dbname="sistema_banco_ocr",
        )

        db_queries = DatabaseQueries(db_connection.conn)

        # TESTE CLASSE IMAGEM==================================
        # path = "C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/Projeto_Ciclo01_AlphaEdtech/images/print_livro.png"
        # image = ImageClass("imagemTeste", image_path=path)

        # image.save_to_database(db_connection)
        # image.show_image()
        # image_r = ImageClass.from_database(db_connection, image.id)
        # image_r.show_image()

        # TESTE CLASSE CLIENTE ========================
        # cliente = Client(
        #     "Ruben",
        #     "12345556",
        #     "9992-33",
        #     "4334120001-9",
        #     "145, Rua cinco, Mondubim, Fortaleza - CE",
        #     date(2023, 4, 10),
        # )
        # cliente.save_to_database(db_connection)
        # cliente2 = Client.from_database(db_connection, cliente.id)
        # print(cliente2)

        # TESTE CLASSE USUARIO ==========================================
        # usuario = User(
        #     "Daniel",
        #     "12345556",
        #     "danielf",
        #     "54321",
        # )
        # usuario.save_to_database(db_connection)
        # usuario2 = User.from_database(db_connection, usuario.id)
        # print(usuario2)

        # TESTE CLASSE DOCUMENTO DIGITAL=====================================================
        # cliente = Client(
        #     "Ruben",
        #     "12345556",
        #     "9992-33",
        #     "4334120001-9",
        #     "145, Rua cinco, Mondubim, Fortaleza - CE",
        #     date(2023, 4, 10),
        # )

        # path = "C:/Users/ruben/Pictures/imagens 4k para fundo de tela/kuzan-one-piece-uhdpaper.com-4K-6.31.jpg"
        # image = ImageClass("imagemTeste", image_path=path)
        # document = DigitalDocument(
        #     "agent1", "gaveta1", date(2024, 2, 12), 2000.00, 12345605, image, cliente
        # )
        # document.save_to_database(db_connection)

        documento_recuperado = DigitalDocument.from_database(db_connection, 1)
        print(documento_recuperado)
        documento_recuperado.image.show_image()

    finally:
        if db_connection.conn:
            db_connection.close_connection()
