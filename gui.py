import csv
import tkinter
import customtkinter
import os
from PIL import Image
import pandas as pd
from investiments import Investments

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.name_of_file = None

        self.title("Desafio ENACOM")
        self.geometry(f"{1300}x{760}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "enacom_logo.png")), size=(26, 26))
        
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Desafio ENACOM", 
                                                             image=self.logo_image, compound="left", 
                                                             font=customtkinter.CTkFont(size=20, weight="bold", 
                                                                                        family="Helvetica"))
        self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=20)

        self.available_invests = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                                         text="Investimentos Disponíveis", fg_color="transparent", 
                                                         text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                         anchor="w", command=self.available_invests_event,
                                                         font=customtkinter.CTkFont(size=17, family="Helvetica"))
        self.available_invests.grid(row=1, column=0, sticky="ew")

        self.my_invests = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                                  text="Meus Investimentos", fg_color="transparent",
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                  anchor="w", command=self.my_invests_event, 
                                                  font=customtkinter.CTkFont(size=17, family="Helvetica"))
        self.my_invests.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light"],
                                                                command=self.change_appearance_mode_event, corner_radius=3,
                                                                height=33, text_color=("gray10", "gray90"),
                                                                font=customtkinter.CTkFont(size=15, family="Helvetica"))
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(0, 35), sticky="s")

        # create home frame
        self.available_invests_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")  
        self.available_invests_frame.grid_columnconfigure(0, weight=1)
        
        # botão buscar arquivo
        self.button1 = customtkinter.CTkButton(self.available_invests_frame, text="Buscar arquivo", 
                                               command=self.file_dialog, corner_radius=10, height=70, width=25,
                                               font= customtkinter.CTkFont(
                                                   size=17, family="Helvetica"))
        self.button1.place(rely=0.80, relx=0.50)

        # botão carregar arquivo
        self.button2 = customtkinter.CTkButton(self.available_invests_frame, text="Carregar arquivo", 
                                               command=self.load_data, corner_radius=10, height=70, width=25,
                                               font= customtkinter.CTkFont(
                                                    size=17, family="Helvetica"
                                                   )
                                            )
        self.button2.place(rely=0.80, relx=0.30)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self.available_invests_frame, width=1100, height=350)
        self.scrollable_frame.grid(row=0, column=0, pady=20, padx=20)

        self.label_file = customtkinter.CTkLabel(self.scrollable_frame, text="Nenhum arquivo selecionado",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_file.grid(row=0, column=1, padx=20, pady=20)

        # create second frame
        self.my_invests_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.my_invests_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        
        self.button3 = customtkinter.CTkButton(self.my_invests_frame, text="Investir",
                                               command=self.start_investing, corner_radius=10, height=60, width=25,
                                               font=customtkinter.CTkFont(size=17, family="Helvetica"))

        self.button3.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.scrollable_frame_2 = customtkinter.CTkScrollableFrame(master=self.my_invests_frame, width=1100, height=350)
        self.scrollable_frame_2.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

        self.label_file_2 = customtkinter.CTkLabel(self.scrollable_frame_2, text="Nenhum arquivo selecionado",
                                                             font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_file_2.grid(row=0, column=1, pady=20, padx=20)

        # default page
        self.select_frame_by_name("available_invests")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.available_invests.configure(fg_color=("gray75", "gray25") if name == "available_invests" else "transparent")
        self.my_invests.configure(fg_color=("gray75", "gray25") if name == "my_invests" else "transparent")

        # show selected frame
        if name == "available_invests":
            self.available_invests_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.available_invests_frame.grid_forget()
        if name == "my_invests":
            self.my_invests_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.my_invests_frame.grid_forget()

    def available_invests_event(self):
        self.select_frame_by_name("available_invests")

    def my_invests_event(self):
        self.select_frame_by_name("my_invests")

    def add_data_event(self):
        self.select_frame_by_name("add_data")

    def file_dialog(self):
        directory = "/home/matheus/Downloads/DESAFIO - Bootcamp seletivo Enacom Group -20230716T032043Z-001/DESAFIO - Bootcamp seletivo Enacom Group /data"
        filename = customtkinter.filedialog.askopenfilename(initialdir=directory,
                                          title="Selecione um arquivo")
        self.label_file.configure(text=filename)

    def load_data(self):
        self.name_of_file = self.label_file.cget("text")
        try:
            if not self.name_of_file.endswith("csv"):
                raise ValueError
            with open(self.name_of_file, "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
                data = list(reader)
        except ValueError:
            tkinter.messagebox.showerror("Erro", "O arquivo selecionado é inválido")
            return
        except FileNotFoundError:
            tkinter.messagebox.showerror("Erro", f"Arquivo não encontrado")
            return

        self.label_file.configure(text="")  # Pensar num título

        col_names = ('Opção','Descrição','Custo de investimento (R$)','Retorno esperado (R$)','Risco')
        for i, col_name in enumerate(col_names, start=1):
            customtkinter.CTkLabel(self.scrollable_frame, text=col_name,
                                   font=customtkinter.CTkFont(
                                       size= 17, weight="bold", family="Helvetica"
                                       )).grid(row=1, column=i, padx=20)

        for i, row in enumerate(data, start=2):
            for col in range(1, 6):
                customtkinter.CTkLabel(self.scrollable_frame, text=row[col - 1],
                                       font=customtkinter.CTkFont(
                                           size=17, family="Helvetica"
                                           )).grid(row=i, column=col, padx=20)

    def start_investing(self):
        try:
            if self.name_of_file is None:
                raise TypeError
            
            if not self.name_of_file.endswith(".csv") or len(self.name_of_file) == 0:
                raise FileNotFoundError

            my_investiments = Investments(self.name_of_file, 1_400_000)
        except ValueError:
            tkinter.messagebox.showerror("Erro", "O arquivo selecionado é inválido")
            return
        except FileNotFoundError:
            tkinter.messagebox.showerror("Erro", f"Arquivo não encontrado")
            return
        except TypeError:
            tkinter.messagebox.showerror("Erro", "Por favor carregue os arquivos na página inicial")
            return

        my_investiments.find_best_solution_at_all()

        with open("MyInvestiments/resultado.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
    
        self.label_file_2.configure(text="")

        col_names = ('Opção','Descrição','Custo de investimento (R$)','Retorno esperado (R$)','Risco')
        for i, col_name in enumerate(col_names, start=1):
            customtkinter.CTkLabel(self.scrollable_frame_2, text=col_name,
                                   font=customtkinter.CTkFont(
                                       size= 17, weight="bold", family="Helvetica"
                                       )).grid(row=1, column=i, padx=20)

        for i, row in enumerate(data, start=2):
            for col in range(1, 6):
                customtkinter.CTkLabel(self.scrollable_frame_2, text=row[col - 1],
                                       font=customtkinter.CTkFont(
                                           size=17, family="Helvetica"
                                           )).grid(row=i, column=col, padx=20)

        aux_invest_frame = customtkinter.CTkFrame(self.my_invests_frame, corner_radius=0, fg_color="transparent")
        aux_invest_frame.grid(row=1, column=1, padx=(0, 0), pady=10, sticky="w")

        low = customtkinter.CTkLabel(aux_invest_frame, 
                               text=f"Investimentos de risco baixo: R$ {my_investiments.get_sum_of_low_invests()}",
                               font=customtkinter.CTkFont(family="Helvetica", size=17, weight="bold"))
        low.grid(row=1, column=1, pady=(0, 0), padx=(0, 0), sticky="w")

        medium = customtkinter.CTkLabel(aux_invest_frame,
                                text=f"Investimentos de risco médio: R$ {my_investiments.get_sum_of_medium_invests()}",
                                font=customtkinter.CTkFont(family="Helvetica", size=17, weight="bold"))
        medium.grid(row=2, column=1, pady=(5, 0), padx=(0, 0), sticky="w")

        high = customtkinter.CTkLabel(aux_invest_frame,
                                text=f"Investimentos de risco alto: R$ {my_investiments.get_sum_of_high_invests()}",
                                font=customtkinter.CTkFont(family="Helvetica", size=17, weight="bold"))
        high.grid(row=3, column=1, pady=(5, 0), padx=(0, 0), sticky="w")

        total_invest_frame = customtkinter.CTkFrame(self.my_invests_frame, corner_radius=0, fg_color="transparent")
        total_invest_frame.grid(row=1, column=2, padx=(0, 0), pady=10, sticky="w")

        total = customtkinter.CTkLabel(total_invest_frame, 
                                       text=f"Retorno esperado total: R$ {my_investiments.get_sum_of_all_investiments()}",
                                       font=customtkinter.CTkFont(family="Helvetica", size=17, weight="bold"))
        total.grid(row=0, column=0, pady=(5, 0), padx=(0, 0), sticky="w")


