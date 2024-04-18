from tkinter import Tk, Canvas, Button, PhotoImage, Frame, ttk, messagebox
from pathlib import Path
import classe_tela_pesquisa
import classe_tela_inicial
import os
from PIL import Image
from pathlib import Path
from io import BytesIO

class TelaMeusArquivos(Tk):
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
            / f"TELAS TKINTER\\TELA_MEUS_ARQUIVOS\\build\\assets\\frame0"
        )
        self.relative_to_assets = lambda path: self.assets_path / Path(path)

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
            bg=self.cget('bg')
        )
        self.button_1.place(x=17.0, y=100.0, width=155.0, height=24.0)

        self.button_image_2 = PhotoImage(file=str(self.assets_path / "button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.ir_tela_pesquisar,
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_2.place(x=17.0, y=138.0, width=124.0, height=24.0)

        self.button_image_3 = PhotoImage(file=str(self.assets_path / "button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
            bg=self.cget('bg')
        )
        self.button_3.place(x=17.0, y=176.0, width=162.0, height=24.0)

        self.image_image_1 = PhotoImage(file=str(self.assets_path / "image_1.png"))
        self.image_1 = self.canvas.create_image(45.0, 43.0, image=self.image_image_1)

        self.canvas.create_text(
            765.0,
            102.0,
            anchor="nw",
            text="Ordenar por:",
            fill="#2E5266",
            font=("Poppins Regular", 16 * -1),
        )

        self.button_image_4 = PhotoImage(file=str(self.assets_path / "button_4.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_4.place(x=945.0, y=102.0, width=24.0, height=24.0)

        self.button_image_5 = PhotoImage(file=str(self.assets_path / "button_5.png"))
        self.button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_5.place(x=907.0, y=102.0, width=24.0, height=24.0)

        self.button_image_6 = PhotoImage(file=str(self.assets_path / "button_6.png"))
        self.button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_6.place(x=773.0, y=162.0, width=93.0, height=29.0)

        self.button_image_7 = PhotoImage(file=str(self.assets_path / "button_7.png"))
        self.button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_7.place(x=898.0, y=162.0, width=93.0, height=29.0)

        self.button_image_8 = PhotoImage(file=str(self.assets_path / "button_8.png"))
        self.button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_8.place(x=838.0, y=260.0, width=93.0, height=29.0)

        self.button_image_9 = PhotoImage(file=str(self.assets_path / "button_9.png"))
        self.button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_9.place(x=897.0, y=209.0, width=93.0, height=29.0)

        self.button_image_10 = PhotoImage(file=str(self.assets_path / "button_10.png"))
        self.button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat",
            bg='#D3D0CB',
            activebackground='#D3D0CB'
        )
        self.button_10.place(x=773.0, y=208.0, width=93.0, height=29.0)

        self.treeview_frame=Frame(self, bd=1, relief="solid", bg="#D9D9D9")
        self.treeview_frame.place(x=205, y=85, width=537, height=435)
        # Adicionando o TreeView ao LabelFrame
        self.treeview = ttk.Treeview(self.treeview_frame, columns=('Nº Cédula', 'Agente', 'Titular', 'Valor','Data'), show='headings')
        self.treeview.heading('Nº Cédula', text='Número da Cédula')
        self.treeview.heading('Agente', text='Agente')
        self.treeview.heading('Titular', text='Titular')
        self.treeview.heading('Valor', text='Valor')
        self.treeview.heading('Data', text='Data de Modificação')
        self.treeview.pack(fill="both", expand=True)  # Preenche todo o espaço disponível

        xscroll = ttk.Scrollbar(self.treeview, orient="horizontal")
        yscroll = ttk.Scrollbar(self.treeview, orient="vertical")

        # Adicionando as barras de rolagem
        xscroll.pack(side="bottom", fill="x")
        yscroll.pack(side="right", fill="y")

        xscroll.config(command=self.treeview.xview)
        yscroll.config(command=self.treeview.yview)

        # Associando as barras de rolagem à treeview
        self.treeview.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        # Lidando com o duplo clique na treeview
        self.treeview.bind("<Double-1>", self.abrir_imagem)

    def abrir_imagem(self, event):
        pass
        #Possível implementação para esta função
        '''
        item = self.treeview.selection()
        if item:
            # Obtém o nome do arquivo do item selecionado
            filename = self.treeview.item(item, "values")[0]
            image_data = self.db.fetch_image(filename)
            if image_data:
                try:
                    # Converte os dados binários da imagem de volta para uma imagem
                    img = Image.open(BytesIO(image_data))
                    img.show()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao abrir imagem: {e}")
            else:
                messagebox.showerror("Erro", f"Imagem correspondente ao arquivo '{filename}' não encontrada.")
            '''

    def run(self):
        self.mainloop()

    def ir_tela_pesquisar(self):
        # Destrua a tela inicial
        self.destroy()
        # Crie uma nova instância da tela de pesquisa e execute
        tela_pesquisa = classe_tela_pesquisa.TelaPesquisa()
        tela_pesquisa.run()

    def ir_para_inicial(self):
        # Destrua a tela de pesquisa
        self.destroy()
        # Crie uma nova instância da tela inicial e execute
        tela_inicial = classe_tela_inicial.TelaInicial()
        tela_inicial.run()