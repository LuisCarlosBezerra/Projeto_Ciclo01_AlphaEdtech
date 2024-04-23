from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, END, messagebox
from pathlib import Path
from PIL import Image, ImageTk
import os
from db.repository import Repository
from models.client import Client
from models.application import DigitalDocument
from models.image import ImageClass

from image_processing.classOCR import OCR


class TelaEdicaoArquivo(Tk):
    """
    A função submter irá pegar o que está escrito nos textboxs, que serão preenchidos pelo OCR, e salvar.
    Para evitar documentos incompletos no banco de dados, será usada uma condição para verificar se um dos campos está
    vazio. Se sim, aparece uma menssagem pedidndo para que o usuário preencha tudo corretamente. Essa é uam medida
    de segurança para evitar erro no banco e para caso o usuário acione o botão de salvar antes dos campos serem
    preenchidos ou, até mesmo, caso ele tenha editado os campos e no processo tenha deixado um em aberto.

    Se a condição for respeitada, a função de enviar o que está escritos nos campos será chamada automaticamente e
    o documento será salvo no banco de dados.
    """

    """
    def submter(self):
        entry_1 = self.entry_1.get()
        entry_2 = self.entry_2.get()
        entry_3 = self.entry_3.get()
        entry_4 = self.entry_4.get()
        entry_5 = self.entry_5.get()
        entry_6 = self.entry_6.get()

        # Verificar se algum campo está vazio
        if not all([entry_1, entry_2, entry_3, entry_4, entry_5, entry_6]):
            # Se algum campo estiver vazio, exibir uma mensagem de erro
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        else:
            # Se todos os campos estiverem preenchidos, enviar os filtros
            self.enviar_campos(entry_1, entry_2, entry_3, entry_4, entry_5, entry_6)

    def enviar_campos(self, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6):
        print("Enviado ao banco")
        
        IMPLEMENTAR LÓGICA OU FUNÇÃO DO OCR QUE IRÁ ENVIAR PARA O BANCO. ELA DEVE RECEBER OS PARAMETROS DESSA FUNÇÃO
        POIS ELA QUE ESTÁ OS TEXTOS E NÚMEROS PREENCHIDOS NOS CAMPOS ATRAVÉS DA INTERFACE.

        SE FOR DISPENSÁVEL ESTA FUNÇÃO, PODE EXCLUÍ-LA, CONTANTO QUE OS CAMPOS SEJAM ENVIADOS
        """

    def __init__(self, file_path, repository: Repository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        ocr = OCR(file_path)
        # self.dict_values = {
        #     "Emitente: ": "Ruben",  # NOME CLIENTE
        #     "CPF: ": "123456",  # CPF CLIENTE
        #     "Dt de Nasc:": "17/07/1999",  # DATA DE NASCIMENTO CLIENTE
        #     "Local: ": "gaveta22",  # DATA CONTRATO
        #     "DATA_CONTRATO": "01/08/2024",
        #     "dereço:": "Marco - rua cinco",  # ENDERECO DO CLIENTE
        #     "Agência nº:": "4563",  # AGENCIA
        #     "Conta nº:": "23456-4",  # CONTA
        #     "anco nº:": "Fire",  # BANCO
        #     "BANCÁRIO Nº": "9876432",  # Nº DA CÉDULA
        #     "$ ": "4000",  # VALOR CRÉDITO
        #     "Nome do Agente:": "Luis",  # NOME DO AGENTE
        #     "CPF do Agente: ": "986763032-93",  # CPF DO AGENTE
        # }
        self.dict_values = ocr.extrairTexto()
        self.file_path = "images/outputs_temp_images/output.png"
        self.agencia = self.dict_values["AGENCIA"]
        self.conta = self.dict_values["CONTA"]
        self.data_nasc = self.dict_values["DATA_CLIENTE:"]
        self.endereco = self.dict_values["ENDERECO"]
        self.cpf = self.dict_values["CPF_CLIENTE"]
        self.layout_config()
        self.appearence()
        self.set_text(
            titular=self.dict_values["NOME_CLIENTE"],
            valor_credito=self.dict_values["VALOR_CREDITO"]
            .replace(",", ".")
            .replace(".", "", 1),
            nome_agente=self.dict_values["NOME_AGENTE"],
            data_contrato=self.dict_values["DATA_CONTRATO"],
            numero_cedula=self.dict_values["CEDULA"],
        )

    def layout_config(self):
        self.title("OCRCreditBank")
        self.geometry("1030x520")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

    def appearence(self):
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=520,
            width=1030,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.output_path = os.path.abspath(os.path.dirname(__file__)).replace(
            "\\CLASSES_TELAS", ""
        )
        self.assets_path = (
            Path(self.output_path)
            / f"TELAS TKINTER\\TELA_EDICAO_ARQUIVO\\build\\assets\\frame0"
        )
        self.relative_to_assets = lambda path: self.assets_path / Path(path)

        # Criar ícone da aplicação para janela
        icon_path = self.relative_to_assets("logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        x_coord = 1030 - 291  # Largura da janela - largura do label
        y_coord = 520 - 418  # Altura da janela - altura do label
        y_coord -= 10
        self.image_label = Label(self, bg="#D3D0CB")
        self.image_label.place(x=x_coord, y=y_coord, width=291, height=418)

        self.canvas.create_rectangle(0.0, 0.0, 1030.0, 85.0, fill="#2E5266", outline="")

        self.canvas.create_text(
            95.0,
            20.0,
            anchor="nw",
            text="OCRCreditBank",
            fill="#FEFEFE",
            font=("Poppins Regular", 32 * -1),
        )

        self.image_image_1 = PhotoImage(file=str(self.assets_path / "image_1.png"))
        self.image_1 = self.canvas.create_image(45.0, 43.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=str(self.assets_path / "image_2.png"))
        self.image_2 = self.canvas.create_image(885.0, 292.0, image=self.image_image_2)

        self.canvas.create_text(
            51.0,
            170.0,
            anchor="nw",
            text="NOME TITULAR (EMITENTE)",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.entry_image_1 = PhotoImage(file=str(self.assets_path / "entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            231.0, 322.5, image=self.entry_image_1
        )
        self.entry_1 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=50.5, y=308.0, width=361.0, height=27.0)

        self.entry_image_2 = PhotoImage(file=str(self.assets_path / "entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            231.0, 451.5, image=self.entry_image_2
        )
        self.entry_2 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=50.5, y=437.0, width=361.0, height=27.0)

        self.canvas.create_text(
            51.0,
            287.0,
            anchor="nw",
            text="VALOR DO CRÉDITO (R$)",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.entry_image_3 = PhotoImage(file=str(self.assets_path / "entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            231.0, 263.5, image=self.entry_image_3
        )
        self.entry_3 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=50.5, y=249.0, width=361.0, height=27.0)

        self.canvas.create_text(
            51.0,
            228.0,
            anchor="nw",
            text="NOME AGENTE          ",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            51.0,
            409.0,
            anchor="nw",
            text="LOCAL FÍSICO DE ARMAZENAMENTO",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.entry_image_4 = PhotoImage(file=str(self.assets_path / "entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            231.0, 204.5, image=self.entry_image_4
        )
        self.entry_4 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=50.5, y=190.0, width=361.0, height=27.0)

        self.canvas.create_text(
            52.0,
            108.0,
            anchor="nw",
            text="N° CÉDULA DE CRÉDITO BANCÁRIO",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.entry_image_5 = PhotoImage(file=str(self.assets_path / "entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            231.0, 144.5, image=self.entry_image_5
        )
        self.entry_5 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=50.5, y=130.0, width=361.0, height=27.0)

        self.button_image_1 = PhotoImage(file=str(self.assets_path / "button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.submter,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_1.place(x=484.0, y=437.0, width=93.0, height=29.0)

        self.button_image_2 = PhotoImage(file=str(self.assets_path / "button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_para_inicial,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_2.place(x=604.0, y=437.0, width=93.0, height=29.0)

        self.entry_image_6 = PhotoImage(file=str(self.assets_path / "entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            231.0, 383.5, image=self.entry_image_6
        )
        self.entry_6 = Entry(bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=50.5, y=369.0, width=361.0, height=27.0)

        self.canvas.create_text(
            51.0,
            348.0,
            anchor="nw",
            text="DATA DO CONTRATO",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            498.0,
            118.0,
            anchor="nw",
            text="PRÉ-VISUALIZAÇÃO DE \n    ARQUIVO E DADOS",
            fill="#000000",
            font=("Poppins Bold", 15 * -1),
        )

    def open_image(self, file_path):
        if file_path:
            image = Image.open(file_path)
            width, height = image.size
            max_size = (291, 418)  # Tamanho do label
            new_width, new_height = width, height

            if width > max_size[0] or height > max_size[1]:
                aspect_ratio = width / height
                if width > height:
                    new_width = max_size[0]
                    new_height = int(new_width / aspect_ratio)
                else:
                    new_height = max_size[1]
                    new_width = int(new_height * aspect_ratio)

            image = image.resize((new_width, new_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def run(self):
        self.open_image(self.file_path)
        self.mainloop()

    def ir_para_inicial(self):
        # Destrua a tela de login
        self.destroy()
        # Crie uma nova instância da tela inicial e execute
        from interfaces.CLASSES_TELAS.classe_tela_inicial import TelaInicial

        tela_inicial = TelaInicial(self.repository)
        tela_inicial.run()

    def submter(self):
        entry_1 = self.entry_1.get()
        entry_2 = self.entry_2.get()
        entry_3 = self.entry_3.get()
        entry_4 = self.entry_4.get()
        entry_5 = self.entry_5.get()
        entry_6 = self.entry_6.get()

        if entry_2 == "":
            messagebox.showerror(
                "Erro: Campo vazio",
                "Campo LOCAL FÍSICO DE ARMAZENAMENTO vazio, por favor Preencha este campo!",
            )
        else:
            self.repository.save_applicacation(
                DigitalDocument(
                    agent_name=entry_3,
                    physical_location=entry_2,
                    contract_date=entry_6,
                    credit_value=entry_1,
                    certificate_number=entry_5,
                    image=ImageClass(
                        image_name="imagem",
                        image_path=self.file_path,
                    ),
                    client=Client(
                        name=entry_4,
                        cpf=self.cpf,
                        agency=self.agencia,
                        account=self.conta,
                        address=self.endereco,
                        birth_date=self.data_nasc,
                    ),
                )
            )
            self.ir_para_inicial()

    def set_text(
        self, valor_credito, titular, nome_agente, data_contrato, numero_cedula
    ):
        self.entry_1.delete(0, END)  # Remove o conteúdo atual
        self.entry_1.insert(0, valor_credito)
        self.entry_6.delete(0, END)  # Remove o conteúdo atual
        self.entry_6.insert(0, data_contrato)
        self.entry_3.delete(0, END)  # Remove o conteúdo atual
        self.entry_3.insert(0, nome_agente)
        self.entry_4.delete(0, END)  # Remove o conteúdo atual
        self.entry_4.insert(0, titular)
        self.entry_5.delete(0, END)  # Remove o conteúdo atual
        self.entry_5.insert(0, numero_cedula)
        self.entry_2.delete(0, END)  # Remove o conteúdo atual
        self.entry_2.insert(0, "")
