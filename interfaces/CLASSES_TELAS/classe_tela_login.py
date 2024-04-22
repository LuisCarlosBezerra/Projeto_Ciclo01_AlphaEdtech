from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from user_DB import DB_NAME, USER, PASSWORD
from db.repository import Repository

"""
Arquivo classe_tela_login.py

Este arquivo contém a definição da classe `TelaLogin`, responsável por criar e configurar a interface de login da 
aplicação. Ele importa os módulos necessários, como `Path` e `os`, bem como diversas classes e funções específicas da 
biblioteca Tkinter para a criação da interface gráfica.

A classe `TelaLogin` é uma subclasse da classe `Tk` do Tkinter, o que permite que ela herde todas as funcionalidades e 
métodos dessa classe para construir a janela de login.

A interface é configurada com elementos visuais como botões, entradas de texto, imagens e textos, utilizando o Canvas 
para organizá-los. Além disso, são realizadas operações para configurar a aparência da 
janela, como definir o título, tamanho, cor de fundo e ícone.

O método `create_elements()` é responsável por criar todos os elementos visuais da tela de login, como retângulos, 
imagens, botões e entradas de texto, posicionando-os corretamente na janela.

Os métodos `submter()`, `ir_para_cadastro()` e `ir_para_inicial()` são responsáveis por lidar com eventos, 
como o clique nos botões de login e cadastro, e realizar ações apropriadas, como verificar as credenciais do usuário e 
redirecioná-lo para outras telas.
"""


class TelaLogin(Tk):
    """
    Chama os métodos layout_config() e appearence() para configurar a aparência da janela e instanciar a classe
    Repository para acesso ao banco de dados.
    """

    def __init__(self, repository: Repository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout_config()
        self.appearence()
        self.repository = repository

    """
    Este método configura o layout da janela de login. Ele define o título da janela como "OCRCreditBank", 
    o tamanho da janela como 778x503 pixels e a cor de fundo como branco (#FFFFFF). Além disso, ele impede que 
    o usuário redimensione a janela.
    """

    def layout_config(self):
        self.title("OCRCreditBank")
        self.geometry("778x503")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

    """
    Responsável por configurar a aparência da janela. Ele cria um Canvas para conter os elementos visuais da tela 
    de login e configura o ícone da aplicação se o arquivo do ícone existir. Em seguida, chama create_elements() 
    para criar os elementos visuais.
    """

    def appearence(self):
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=503,
            width=778,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.output_path = os.path.abspath(os.path.dirname(__file__)).replace(
            "\\CLASSES_TELAS", ""
        )
        self.assets_path = (
            Path(self.output_path) / f"TELAS TKINTER\\TELA_LOGIN\\build\\assets\\frame0"
        )
        self.relative_to_assets = lambda path: self.assets_path / Path(path)

        # Criar ícone da aplicação para janela
        icon_path = self.relative_to_assets("logo.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        self.create_elements()

    """
    Este método cria todos os elementos visuais da tela de login, como retângulos, imagens, botões e entradas de texto. 
    Ele utiliza o Canvas para desenhar os elementos e posicioná-los corretamente na janela.
    """

    def create_elements(self):
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            141.0,
            314.938720703125,
            171.9011116027832,
            344.46924018859863,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            201.373779296875,
            314.9044189453125,
            243.01795959472656,
            326.9955863952637,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            211.375,
            314.9044189453125,
            258.00003814697266,
            344.4691734313965,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            235.0,
            314.9044189453125,
            285.0,
            340.9999599456787,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            309.42724609375, 327.0, 355.4319610595703, 345.0, fill="#000000", outline=""
        )

        self.canvas.create_rectangle(
            496.0,
            314.771728515625,
            530.9999923706055,
            344.8672695159912,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            327.734619140625,
            295.0,
            384.4624786376953,
            336.0,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(
            398.113037109375,
            302.1787109375,
            459.0,
            344.57861328125,
            fill="#000000",
            outline="",
        )

        self.canvas.create_rectangle(0.0, 0.0, 778.0, 503.0, fill="#2E5266", outline="")

        self.canvas.create_rectangle(
            271.0, 0.0, 778.0, 503.0, fill="#FFFFFF", outline=""
        )

        self.images = {}
        self.images["button_1"] = PhotoImage(
            file=self.relative_to_assets("button_1.png")
        )
        self.images["button_2"] = PhotoImage(
            file=self.relative_to_assets("button_2.png")
        )
        self.images["image_1"] = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(143.0, 247.0, image=self.images["image_1"])

        self.images["image_2"] = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(527.0, 166.0, image=self.images["image_2"])

        self.images["image_3"] = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(527.0, 252.0, image=self.images["image_3"])

        self.images["image_4"] = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(712.0, 50.0, image=self.images["image_4"])

        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(529.5, 207.0, image=entry_image_1)
        self.entry_1 = Entry(bd=1, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=342.0, y=188.0, width=375.0, height=36.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(527.5, 291.0, image=entry_image_2)
        self.entry_2 = Entry(
            bd=1, bg="#FFFFFF", fg="#000716", highlightthickness=0, show="*"
        )
        self.entry_2.place(x=340.0, y=272.0, width=375.0, height=36.0)

        button_1 = Button(
            self,  # Adicionando à janela principal, não ao canvas
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.submter,
            relief="flat",
            bg=self.cget("bg"),
        )
        button_1.place(x=593.0, y=389.0, width=110.0, height=35.0)

        # button_2 = Button(
        #     self,
        #     image=self.images["button_2"],
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=print("click"),
        #     relief="flat",
        #     bg=self.cget("bg"),
        # )
        # button_2.place(x=501.0, y=319.0, width=105.0, height=24.0)

        # text1 = self.canvas.create_text(
        #     327.0,
        #     319.0,
        #     anchor="nw",
        #     text="Não tem uma conta?",
        #     fill="#000000",
        #     font=("Poppins Regular", 16 * -1),
        # )

        text2 = self.canvas.create_text(
            327.0,
            90.0,
            anchor="nw",
            text="Faça login para continuar",
            fill="#000000",
            font=("Poppins Bold", 16 * -1),
        )

    """
    Chamado quando o botão de submissão é clicado. Ele obtém o nome de usuário e a senha inseridos pelo usuário e 
    tenta fazer login chamando o método login() da instância de Repository. 
    Se o login for bem-sucedido, redireciona o usuário para a tela inicial; caso contrário, exibe uma mensagem de erro.
    """

    def submter(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        if self.repository.login(username, password):
            self.ir_para_inicial(username)
        else:
            messagebox.showerror(
                "Erro", "Usuário ou senha incorretos. Por favor, tente novamente."
            )

    """
    Chamado quando o login é bem-sucedido. Ele destrói a tela de login atual e cria uma nova instância da tela inicial 
    da aplicação.
    """

    def ir_para_inicial(self, username):
        self.destroy()
        from interfaces.CLASSES_TELAS.classe_tela_inicial import TelaInicial

        chamar_tela_inicial = TelaInicial(self.repository)
        chamar_tela_inicial.run()

    """
    Inicia o loop principal da interface gráfica, permitindo que a aplicação seja executada e interaja com o usuário.
    """

    def run(self):
        self.mainloop()
