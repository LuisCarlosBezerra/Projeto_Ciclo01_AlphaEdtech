# from db.connection import DatabaseConnection
from db.repository import Repository

# from models.image import ImageClass
from models.client import Client

# from models.user import User

from models.digital_document import DigitalDocument
from models.application import Application
from datetime import date, datetime
from user_DB import DB_NAME, USER, PASSWORD


if __name__ == "__main__":
    try:
        repository = Repository(
            user=USER,
            password=PASSWORD,
            dbname=DB_NAME,
        )
        db = repository.db

        # TESTE CLASSE APLICAÇÃO=======================================================
        cliente = Client(
            "Liane",
            "12345556",
            "9992-33",
            "4334120001-9",
            "145, Rua cinco, Centro, Pereiras - CE",
            date(2023, 4, 10),
        )
        # usuario = User(
        #     "Usuario2",
        #     "12345556",
        #     "user2",
        #     "54321",
        # )

        # path = "C:/Users/ruben/Pictures/imagens 4k para fundo de tela/10.jpg"
        # image = ImageClass("imagemKimetsuRaio", image_path=path)
        # document = DigitalDocument(
        #     "agent3", "gaveta3", date(2024, 3, 12), 5000.00, 12345605, image, cliente
        # )
        # aplicacao = Application(
        #     "Inserindo Cedula Bancaria",
        #     datetime(2024, 2, 28, 8, 36, 2),
        #     usuario,
        #     document,
        # )
        # repository.save_applicacation(aplicacao)
        # aplicacao_rec = repository.get_application(2)
        # print(aplicacao_rec)
        # aplicacao_rec.digital_document.image.show_image()

        # TESTE DA BUSCA DOS CLIENTES PELO NOME.
        # clientes = Client.from_database_by_name(db, "R", class_document=DigitalDocument)
        # print(clientes)
        # ------------------------------------------------------------------------------------------
        # TESTE DA BUSCA DOS CLIENTES PELO NÚMERO DA CÉDULA.
        ##### TESTE COM A FUNÇÃO QUE RETORNA UMA LISTA DE DOCUMENTOS CUJO OS NÚMEROS DE
        ##### CÉDULAS CONTÉM O NÚMERO INFORMADO COMO ARGUMENTO.
        # documentos = DigitalDocument.array_from_db_by_certificate_number(db, 1)
        # documentos[1].image.show_image()
        # print(documentos[1])
        ##### TESTE COM A FUNÇÃO QUE RETORNA UM DOCUMENTO CUJO O NÚMERO DE
        ##### CÉDULA É IGUAL AO NÚMERO INFORMADO COMO ARGUMENTO.
        # documento = DigitalDocument.from_db_by_certificate_number(db, "12345605")
        # documento.image.show_image()
        # print(documento)

        # TESTE COM A BUSCA PODENDO USAR O VALOR DE CRÉDITO, O NOME DO AGENTE, A DATA DE CONTRATO E
        # O NOME DO CLIENTE.
        documentos = repository.get_document_by_choice(
            # cr_value_init=2000,
            # cr_value_last=5000,
            # ag_name="a",
            # ct_date_init="2024-02-12",
            # ct_date_last="2024-04-12",
            cl_name="a",
        )
        print(documentos[0])
        print(documentos[1])

    finally:
        pass
