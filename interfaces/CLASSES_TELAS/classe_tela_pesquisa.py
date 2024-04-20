from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, ttk, messagebox
from pathlib import Path
import os
from db.repository import Repository


class TelaPesquisa(Tk):
    def __init__(self, repository: Repository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = repository
        self.layout_config()
        self.appearence()

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
            / f"TELAS TKINTER\\TELA_PESQUISA\\build\\assets\\frame0"
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

        self.canvas.create_rectangle(
            205.0, 85.0, 702.0, 520.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_text(
            94.0,
            21.0,
            anchor="nw",
            text="OCRCreditBank",
            fill="#FEFEFE",
            font=("Poppins Regular", 32 * -1),
        )

        self.button_image_1 = PhotoImage(file=str(self.assets_path / "button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_para_inicial,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_1.place(x=17.0, y=100.0, width=155.0, height=24.0)

        self.button_image_2 = PhotoImage(file=str(self.assets_path / "button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_2.place(x=17.0, y=138.0, width=124.0, height=24.0)

        self.button_image_3 = PhotoImage(file=str(self.assets_path / "button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_meus_arquivos,
            relief="flat",
            bg=self.cget("bg"),
        )
        self.button_3.place(x=17.0, y=176.0, width=162.0, height=24.0)

        self.image_image_1 = PhotoImage(file=str(self.assets_path / "image_1.png"))
        self.image_1 = self.canvas.create_image(45.0, 43.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=str(self.assets_path / "image_2.png"))
        self.image_2 = self.canvas.create_image(796.0, 108.0, image=self.image_image_2)

        self.button_image_4 = PhotoImage(file=str(self.assets_path / "button_4.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.submter,
            relief="flat",
            bg="#D3D0CB",
            activebackground="#D3D0CB",
        )
        self.button_4.place(x=895.0, y=431.0, width=93.0, height=29.0)

        self.button_image_5 = PhotoImage(file=str(self.assets_path / "button_5.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.limpar,
            relief="flat",
            bg="#D3D0CB",
            activebackground="#D3D0CB",
        )
        self.button_5.place(x=772.0, y=431.0, width=93.0, height=29.0)

        self.entry_image_1 = PhotoImage(file=str(self.assets_path / "entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            873.0, 168.0, image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_1.place(x=774.0, y=152.0, width=198.0, height=30.0)

        self.entry_image_2 = PhotoImage(file=str(self.assets_path / "entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            873.0, 219.0, image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_2.place(x=774.0, y=203.0, width=198.0, height=30.0)

        self.entry_image_3 = PhotoImage(file=str(self.assets_path / "entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            873.0, 270.0, image=self.entry_image_3
        )
        self.entry_3 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_3.place(x=774.0, y=254.0, width=198.0, height=30.0)

        self.entry_image_4 = PhotoImage(file=str(self.assets_path / "entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            816.0, 331.0, image=self.entry_image_4
        )
        self.entry_4 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_4.place(x=778.0, y=315.0, width=76.0, height=30.0)

        self.entry_image_5 = PhotoImage(file=str(self.assets_path / "entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            816.0, 399.0, image=self.entry_image_5
        )
        self.entry_5 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_5.place(x=778.0, y=383.0, width=76.0, height=30.0)

        self.entry_image_6 = PhotoImage(file=str(self.assets_path / "entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            931.0, 331.0, image=self.entry_image_6
        )
        self.entry_6 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_6.place(x=893.0, y=315.0, width=76.0, height=30.0)

        self.entry_image_7 = PhotoImage(file=str(self.assets_path / "entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            931.0, 399.0, image=self.entry_image_7
        )
        self.entry_7 = Entry(
            self.canvas, bd=0, bg="#FEFEFE", fg="#000716", highlightthickness=0
        )
        self.entry_7.place(x=893.0, y=383.0, width=76.0, height=30.0)

        self.canvas.create_text(
            772.0,
            132.0,
            anchor="nw",
            text="N° CÉDULA",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            772.0,
            183.0,
            anchor="nw",
            text="TITULAR",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            772.0,
            235.0,
            anchor="nw",
            text="AGENTE",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            842.0,
            289.0,
            anchor="nw",
            text="VALORES (R$)",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.canvas.create_text(
            817.0,
            353.0,
            anchor="nw",
            text="DATAS (DD/MM/AAAA)",
            fill="#000000",
            font=("Poppins Light", 13 * -1),
        )

        self.treeview_frame = Frame(self, bd=1, relief="solid", bg="#D9D9D9")
        self.treeview_frame.place(x=205, y=85, width=537, height=435)
        # Adicionando o TreeView ao LabelFrame
        self.treeview = ttk.Treeview(
            self.treeview_frame,
            columns=(
                "ID",
                "Titular",
                "Agente",
                "Local Físico Armaz.",
                "Data do Contrato",
                "Valor",
                "Nº Cédula",
            ),
            show="headings",
        )

        # self.treeview.heading("ID", text="ID")
        # self.treeview.heading("Titular", text="Titular")
        # self.treeview.heading("Agente", text="Agente")
        # self.treeview.heading("Local Físico", text="Local Físico Armaz.")
        # self.treeview.heading("Data", text="Data do Contrato")
        # self.treeview.heading("Valor", text="Valor")
        # self.treeview.heading("Nº Cédula", text="Número da Cédula")

        # Definindo as âncoras das colunas como centralizadas e ajustando a largura automaticamente
        for coluna in self.treeview["columns"]:
            self.treeview.heading(coluna, text=coluna, anchor="center")
            self.treeview.column(coluna, anchor="center", width=100,  stretch=True)  # Largura inicial 100, mas que se adapta aos valores fornecidos
        
        self.treeview.pack(
            fill="both", expand=True
        )  # Preenche todo o espaço disponível

        xscroll = ttk.Scrollbar(self.treeview, orient="horizontal")
        yscroll = ttk.Scrollbar(self.treeview, orient="vertical")
        self.treeview.bind("<Double-1>", self.mostrar_imagem)

        # Adicionando as barras de rolagem
        xscroll.pack(side="bottom", fill="x")
        yscroll.pack(side="right", fill="y")

        xscroll.config(command=self.treeview.xview)
        yscroll.config(command=self.treeview.yview)

        # Associando as barras de rolagem à treeview
        self.treeview.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

    def run(self):
        self.mainloop()

    def ir_para_inicial(self):
        # Destrua a tela de pesquisa
        self.destroy()
        # Crie uma nova instância da tela inicial e execute
        from interfaces.CLASSES_TELAS.classe_tela_inicial import TelaInicial

        tela_inicial = TelaInicial(self.repository)
        tela_inicial.run()

    def ir_tela_meus_arquivos(self):
        # Destrua a tela de pesquisa
        self.destroy()
        # Crie uma nova instância da tela de meus arquivos e execute
        from interfaces.CLASSES_TELAS.classe_tela_meus_arquivos import TelaMeusArquivos

        tela_meus_arquivos = TelaMeusArquivos(self.repository)
        tela_meus_arquivos.run()

    def limpar(self):
        self.entry_1.delete(0, "end")
        self.entry_2.delete(0, "end")
        self.entry_3.delete(0, "end")
        self.entry_4.delete(0, "end")
        self.entry_5.delete(0, "end")
        self.entry_6.delete(0, "end")
        self.entry_7.delete(0, "end")

    def submter(self):
        entry_1 = self.entry_1.get()
        entry_2 = self.entry_2.get()
        entry_3 = self.entry_3.get()
        entry_4 = self.entry_4.get()
        entry_5 = self.entry_5.get()
        entry_6 = self.entry_6.get()
        entry_7 = self.entry_7.get()
        items = self.treeview.get_children()
        if len(items) != 0:
            for item in items:
                self.treeview.delete(item)
        self.enviar_filtros(
            entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7
        )

    def enviar_filtros(
        self, c_number, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7
    ):

        print("Enviado filtros")

        if c_number != "":
            document = self.repository.get_document_by_certificate_number(c_number)
            print("dentro do if com vazio")
            if document:
                self.treeview.insert(
                    "",
                    "end",
                    values=(
                        document.id,
                        document.client.name,
                        document.agent_name,
                        document.physical_location,
                        document.contract_date,
                        document.credit_value,
                        document.certificate_number,
                    ),
                )
        else:
            documents = self.repository.get_document_by_choice(
                cl_name=entry_2,
                ag_name=entry_3,
                cr_value_init=entry_4,
                cr_value_last=entry_6,
                ct_date_init=entry_5,
                ct_date_last=entry_7,
            )
            if documents:
                for document in documents:
                    self.treeview.insert(
                        "",
                        "end",
                        values=(
                            document.id,
                            document.client.name,
                            document.agent_name,
                            document.physical_location,
                            document.contract_date,
                            document.credit_value,
                            document.certificate_number,
                        ),
                    )

    def mostrar_imagem(self, event):
        item = self.treeview.selection()
        if item:
            # Obtém o nome do arquivo do item selecionado
            filename = self.treeview.item(item, "values")[0]
            if filename:
                try:
                    document = self.repository.get_document_id(int(filename))
                    document.image.show_image()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao abrir a imagem: {e}")
            else:
                messagebox.showerror("Erro", "Nenhum documento selecionado.")
