from db.connection import DatabaseConnection
from db.repository import DatabaseQueries

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
        # result = db_queries.insert_image(
        #     image_path="C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/Projeto_Ciclo01_AlphaEdtech/imagens-teste/cedula-banco-daycoval-menor.png",
        #     image_name="imagem.jpg",
        # )

        # if result:
        #     print("INFO: Imagem inserida com sucesso!")
        # else:
        #     print("INFO: Falha ao inserir imagem.")
        db_queries.read_image(1)
    finally:
        if connection:
            db_connection.disconnect(connection)
