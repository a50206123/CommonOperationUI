import sys
import customtkinter as ctk
import tkinter as tk
from yc_etabs_api.etabs import ETABS
from gui_loading import LoadingUI
import cmd_main as cmd

class CommonOperationUI :
    def __init__(self) -> None:
        self.etabs = None

        ctk.set_appearance_mode('dark') 
        # ctk.set_default_color_theme()

        app = ctk.CTk()
        app.geometry('640x480')
        app.title('ETABS Faster by YuChen Lin')
        
        app.grid_rowconfigure(0,)
        app.grid_rowconfigure(1,)
        app.grid_rowconfigure(2)
        app.grid_rowconfigure(3)
        app.grid_rowconfigure(4)
        app.grid_columnconfigure(0, weight=3)
        app.grid_columnconfigure(1, weight=0)
        app.grid_columnconfigure(2, weight=3)

        btn_connect = ctk.CTkButton(app, text="Connect to ETABS", width=600, command=self.connect_etabs)
        btn_connect.grid(row=0, column=0, columnspan = 3, padx=20, pady=(20, 0))
        
        label_show_path = ctk.CTkLabel(app, text="")
        label_show_path.grid(row=1, column=0, columnspan = 3, padx=20, pady=0)

        btn_release_i = ctk.CTkButton(app, text="Release I", command=self.release_i, height = 20)
        btn_release_i.grid(row=2, column=0, padx=0, pady=5)
        btn_release_j = ctk.CTkButton(app, text="Release J", command=self.release_j, height = 20)
        btn_release_j.grid(row=2, column=1, padx=0, pady=5)
        btn_release_ij = ctk.CTkButton(app, text="Release IJ", command=self.release_ij, height = 20)
        btn_release_ij.grid(row=2, column=2, padx=0, pady=5)

        btn_loading = ctk.CTkButton(app, text="Click Me to Loading", command=self.open_loading)
        btn_loading.grid(row=3, column=0, padx=0, pady=5)

        self.tb = ctk.CTkTextbox(app)
        self.tb.grid(row=4, column=0)
        sys.stdout = self # To show print messages
        sys.stderr = self # To show error messages

        self.app = app
        self.btn_connect = btn_connect
        self.btn_release_i = btn_release_i
        self.btn_release_j = btn_release_j
        self.btn_release_ij = btn_release_ij
        self.label_show_path = label_show_path

        app.mainloop()
    
    def connect_etabs(self) :
        self = cmd.connect_etabs(self)
    
    def release_i(self) :
        self = cmd.release_i(self)
    
    
    def release_j(self) :
        self = cmd.release_j(self)

    
    def release_ij(self) :
        self = cmd.release_ij(self)

    def open_loading(self) :
        self.Loading = LoadingUI(self.etabs)

    # Callback function for text
    def write(self, txt) :
        self.tb.insert(tk.END, txt)     
        self.tb.see(tk.END)

if __name__ == '__main__' :
    app = CommonOperationUI()

