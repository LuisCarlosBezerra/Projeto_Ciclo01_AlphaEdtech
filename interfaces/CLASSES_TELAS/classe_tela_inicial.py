from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox
from pathlib import Path
import os
from db.repository import Repository
from user_DB import DB_NAME, USER, PASSWORD


class TelaInicial(Tk):
    def __init__(self, repository: Repository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout_config()
        self.appearence(repository.user.user_name)
        self.repository = repository

    def layout_config(self):
        self.title("OCRCreditBank")
        self.geometry("1030x520")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

    def appearence(self, username):
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

        # Criar ícone da aplicação para janela
        icon_path = self.relative_to_assets("logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

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
            bg="#D3D0CB",
            activebackground="#D3D0CB",
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
            bg=self.cget("bg"),
        )
        self.button_2.place(x=17.0, y=100.0, width=155.0, height=24.0)

        self.button_image_3 = PhotoImage(file=str(self.assets_path / "button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_pesquisar,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_3.place(x=17.0, y=138.0, width=124.0, height=24.0)

        self.button_image_4 = PhotoImage(file=str(self.assets_path / "button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_meus_arquivos,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_4.place(x=17.0, y=176.0, width=162.0, height=24.0)

        self.button_image_5 = PhotoImage(file=str(self.assets_path / "button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_5.place(x=47.0, y=244.0, width=110.0, height=35)

        self.canvas.create_text(
            300.0,
            172.0,
            anchor="nw",
            text=f"Seja bem vindo(a), {username}!\n\nAdicione uma imagem ao lado \npara extrair os dados dela.",
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
        self.destroy()
        from interfaces.CLASSES_TELAS.classe_tela_edicao_arquivo import (
            TelaEdicaoArquivo,
        )

        tela_edicao_arquivo = TelaEdicaoArquivo(file_path, self.repository)
        tela_edicao_arquivo.run()

    def ir_tela_pesquisar(self):
        self.destroy()
        from interfaces.CLASSES_TELAS.classe_tela_pesquisa import TelaPesquisa

        tela_pesquisa = TelaPesquisa(self.repository)
        tela_pesquisa.run()

    def ir_tela_meus_arquivos(self):
        self.destroy()
        from interfaces.CLASSES_TELAS.classe_tela_meus_arquivos import TelaMeusArquivos

        tela_meus_arquivos = TelaMeusArquivos(self.repository)
        tela_meus_arquivos.run()

    def logout(self):
        # Destrói a tela inicial e fecha o programa
        self.destroy()
