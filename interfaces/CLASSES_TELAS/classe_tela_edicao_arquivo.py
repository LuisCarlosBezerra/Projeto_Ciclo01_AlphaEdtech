from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
from pathlib import Path
from PIL import Image, ImageTk
import os

class TelaEdicaoArquivo(Tk):
    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self.layout_config()
        self.appearence()

    def layout_config(self):
        self.title('OCRCreditBank')
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
            command=self.ir_para_inicial,
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_1.place(x=484.0, y=437.0, width=93.0, height=29.0)

        self.button_image_2 = PhotoImage(file=str(self.assets_path / "button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_para_inicial,
            relief="flat",
            bg=self.cget('bg')
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
        tela_inicial = TelaInicial()
        tela_inicial.run()
