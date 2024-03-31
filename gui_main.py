import sys
import customtkinter as ctk
import tkinter as tk
from yc_etabs_api.etabs import ETABS
from gui_loading import LoadingUI
# from cmd_section import SectionUI

ui_width = 621

import cmd_main as cmd

class CommonOperationUI :
    def __init__(self) -> None:
        self.etabs = None

        self.initUI()

    
    def initUI(self) :
        ctk.set_appearance_mode('dark') 
        ctk.set_default_color_theme("dark-blue")

        app = ctk.CTk()
        app.geometry('640x480')
        app.title('ETABS Faster by YuChen Lin')

        frame_1 = ctk.CTkFrame(app, width=ui_width)
        frame_1.pack()
        frame_2 = ctk.CTkFrame(app, width=ui_width)
        frame_2.pack()

        #### Frame-1
        label_show_path = ctk.CTkLabel(frame_1, text=" ", width=ui_width)
        label_show_path.pack()
        
        btn_connect = ctk.CTkButton(frame_1, text="Connect to ETABS", command=self.connect_etabs, width=ui_width)
        btn_connect.pack()

        #### Frame-2
        ##### Frame 2-1
        frame_2_1 = ctk.CTkFrame(frame_2, width=ui_width/3)
        frame_2_1.grid(row=0, column=0)
        ##### Frame-2-1-1
        label_2_1_1 = ctk.CTkLabel(frame_2_1, text='Fast Release')
        label_2_1_1.pack()
        frame_2_1_1 = ctk.CTkFrame(frame_2_1)
        frame_2_1_1.pack()

        btn_release_i = ctk.CTkButton(frame_2_1_1, text="Release I", command=self.release_i, height = 20, width=ui_width/3)
        btn_release_i.grid(row=0, column=0, padx=0, pady=0)
        btn_release_j = ctk.CTkButton(frame_2_1_1, text="Release J", command=self.release_j, height = 20, width=ui_width/3)
        btn_release_j.grid(row=1, column=0, padx=0, pady=0)
        btn_release_ij = ctk.CTkButton(frame_2_1_1, text="Release IJ", command=self.release_ij, height = 20, width=ui_width/3)
        btn_release_ij.grid(row=2, column=0, padx=0, pady=0)

        ##### Frame-2-1-2
        label_2_1_2 = ctk.CTkLabel(frame_2_1, text='\nAlways Do those')
        label_2_1_2.pack()
        frame_2_1_2 = ctk.CTkFrame(frame_2_1)
        frame_2_1_2.pack()        

        btn_reduJ = ctk.CTkButton(frame_2_1_2, text="Torsion Reduction", command=self.reduction_torsion, height = 20, width=ui_width/3)
        btn_reduJ.grid(row=0, column=0, padx=0, pady=0)
        btn_set_rz = ctk.CTkButton(frame_2_1_2, text="Set Rigidzone", command=self.set_rz, height = 20, width=ui_width/3)
        btn_set_rz.grid(row=1, column=0, padx=0, pady=0)
        btn_sb_nonsway = ctk.CTkButton(frame_2_1_2, text="SB,FB Nonsway", command=self.sb_nonsway, height = 20, width=ui_width/3)
        btn_sb_nonsway.grid(row=2, column=0, padx=0, pady=0)

        ##### Frame 2-2
        frame_2_2 = ctk.CTkFrame(frame_2, width=ui_width/3)
        frame_2_2.grid(row=0, column=1)

        ##### Frame 2-3
        frame_2_3 = ctk.CTkFrame(frame_2, width=ui_width/3)
        frame_2_3.grid(row=0, column=2)

        btn_loading = ctk.CTkButton(frame_2_3, text="Click Me to Loading", command=self.open_loading, width=ui_width/3)
        btn_loading.grid(row=3, column=0, padx=0, pady=5)

        ##### Frame 3
        self.tb = ctk.CTkTextbox(app, width=ui_width)
        self.tb.pack()
        sys.stdout = self # To show print messages
        sys.stderr = self # To show error messages

        self.app = app
        self.btn_connect = btn_connect
        self.btn_release_i = btn_release_i
        self.btn_release_j = btn_release_j
        self.btn_release_ij = btn_release_ij
        self.label_show_path = label_show_path

        self.Loading = None

        app.mainloop()
    
    # Callback function for text
    def write(self, txt) :
        self.tb.insert(tk.END, txt)     
        self.tb.see(tk.END)
        
    def connect_etabs(self) :
        self = cmd.connect_etabs(self)
    
    def release_i(self) :
        self = cmd.release_i(self)
    
    
    def release_j(self) :
        self = cmd.release_j(self)

    
    def release_ij(self) :
        self = cmd.release_ij(self)

    def reduction_torsion(self) :
        self = cmd.reduction_torsion(self)

    def set_rz(self) :
        self = cmd.set_rz(self)
    
    def sb_nonsway(self) :
        self = cmd.sb_nonsway(self)

    def open_loading(self) :
        self.Loading = LoadingUI(self.etabs)


if __name__ == '__main__' :
    app = CommonOperationUI()

