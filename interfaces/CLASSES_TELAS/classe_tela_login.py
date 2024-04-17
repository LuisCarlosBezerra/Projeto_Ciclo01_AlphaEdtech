from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import classe_tela_cadastro
import classe_tela_inicial


class TelaLogin(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout_config()
        self.appearence()

    def layout_config(self):
        self.title("Projeto")
        self.geometry("778x503")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

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
            "\CLASSES_TELAS", ""
        )
        self.assets_path = (
            Path(self.output_path) / f"TELAS TKINTER\TELA_LOGIN\\build\\assets\\frame0"
        )
        self.relative_to_assets = lambda path: self.assets_path / Path(path)

        self.create_elements()

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

        # Repita o mesmo para as outras imagens

        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(529.5, 207.0, image=entry_image_1)
        entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        entry_1.place(x=342.0, y=188.0, width=375.0, height=36.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(527.5, 291.0, image=entry_image_2)
        entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        entry_2.place(x=340.0, y=272.0, width=375.0, height=36.0)

        # Adicione as outras entradas e botões aqui

        button_1 = Button(
            self,  # Adicionando à janela principal, não ao canvas
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_para_inicial,
            relief="flat",
        )
        button_1.place(x=593.0, y=389.0, width=110.0, height=35.0)

        button_2 = Button(
            self,
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_para_cadastro,
            relief="flat",
        )
        button_2.place(x=501.0, y=319.0, width=105.0, height=24.0)

        text1 = self.canvas.create_text(
            327.0,
            319.0,
            anchor="nw",
            text="Não tem uma conta?",
            fill="#000000",
            font=("Poppins Regular", 16 * -1),
        )

        text2 = self.canvas.create_text(
            327.0,
            90.0,
            anchor="nw",
            text="Faça login para continuar",
            fill="#000000",
            font=("Poppins Bold", 16 * -1),
        )

    def ir_para_cadastro(self):
        # Destrua a tela de login
        self.destroy()
        # Crie uma nova instância da tela de cadastro e execute
        tela_cadastro = classe_tela_cadastro.TelaCadastro()
        tela_cadastro.run()

    def ir_para_inicial(self):
        # Destrua a tela de login
        self.destroy()
        # Crie uma nova instância da tela inicial e execute
        tela_inicial = classe_tela_inicial.TelaInicial()
        tela_inicial.run()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = TelaLogin()
    app.run()
