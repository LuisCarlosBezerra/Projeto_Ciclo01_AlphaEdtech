from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox
from pathlib import Path
import classe_tela_edicao_arquivo
import classe_tela_pesquisa
import classe_tela_meus_arquivos
import os


class TelaInicial(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            / f"TELAS TKINTER\\TELA_INICIAL\\build\\assets\\frame0"
        )
        self.relative_to_assets = lambda path: self.assets_path / Path(path)

        self.canvas.create_rectangle(0.0, 0.0, 1030.0, 85.0, fill="#2E5266", outline="")

        self.canvas.create_rectangle(
            739.0, 85.0, 1030.0, 520.0, fill="#D3D0CB", outline=""
        )

        self.button_image_1 = PhotoImage(file=str(self.assets_path / "button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_image,
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_1.place(x=840.0, y=244.0, width=100.0, height=100.0)

        self.canvas.create_text(
            776.0,
            162.0,
            anchor="nw",
            text="Adicione um arquivo de\ncédula de crédito aqui",
            fill="#FEFEFE",
            font=("Poppins Regular", 19 * -1),
        )

        self.canvas.create_text(
            94.0,
            21.0,
            anchor="nw",
            text="OCRCreditBank",
            fill="#FEFEFE",
            font=("Poppins Regular", 32 * -1),
        )

        self.button_image_2 = PhotoImage(file=str(self.assets_path / "button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_2.place(x=17.0, y=100.0, width=155.0, height=24.0)

        self.button_image_3 = PhotoImage(file=str(self.assets_path / "button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_pesquisar,
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_3.place(x=17.0, y=138.0, width=124.0, height=24.0)

        self.button_image_4 = PhotoImage(file=str(self.assets_path / "button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_meus_arquivos,
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_4.place(x=17.0, y=176.0, width=162.0, height=24.0)

        self.canvas.create_text(
            300.0,
            172.0,
            anchor="nw",
            text="Seja bem vindo(a), Fulano!\n\nAdicione uma imagem ao lado \npara extrair os dados dela.",
            fill="#000000",
            font=("Poppins Regular", 20 * -1),
        )

        self.image_image_1 = PhotoImage(file=str(self.assets_path / "image_1.png"))
        self.image_1 = self.canvas.create_image(45.0, 43.0, image=self.image_image_1)

    def run(self):
        self.mainloop()

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Verifica a extensão do arquivo para garantir que seja uma imagem
            _, file_extension = os.path.splitext(file_path)
            if file_extension.lower() in [".jpg", ".jpeg", ".png"]:
                print("Selected image:", file_path)
                self.ir_tela_edicao_arquivo(file_path)
            else:
                messagebox.showerror(
                    "Erro", "Por favor, selecione um arquivo de imagem válido."
                )

    def ir_tela_edicao_arquivo(self, file_path):
        # Destrói a tela inicial
        self.destroy()
        # Cria uma nova instância da tela de edição de arquivo e execute
        tela_edicao_arquivo = classe_tela_edicao_arquivo.TelaEdicaoArquivo(file_path)
        tela_edicao_arquivo.run()

    def ir_tela_pesquisar(self):
        # Destrói a tela inicial
        self.destroy()
        # Cria uma nova instância da tela de pesquisa e execute
        tela_pesquisa = classe_tela_pesquisa.TelaPesquisa()
        tela_pesquisa.run()

    def ir_tela_meus_arquivos(self):
        # Destrói a tela inicial
        self.destroy()
        # Cria uma nova instância da tela de meus arquivos e execute
        tela_meus_arquivos = classe_tela_meus_arquivos.TelaMeusArquivos()
        tela_meus_arquivos.run()
