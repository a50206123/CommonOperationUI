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
        ctk.set_default_color_theme("gui_theme.json")
        ctk.FontManager.load_font('consola.ttf')

        self.app = ctk.CTk()
        self.app.geometry('640x480')
        self.app.title('ETABS Faster by YuChen Lin')

        self.frame_1 = ctk.CTkFrame(self.app, width=ui_width)
        self.frame_1.pack()
        self.frame_2 = ctk.CTkFrame(self.app, width=ui_width)
        self.frame_2.pack()
        self.frame_3 = ctk.CTkFrame(self.app)
        self.frame_3.pack()

        #### Frame-1
        self.label_show_path = ctk.CTkLabel(self.frame_1, text=" ", width=ui_width, font=('consolas',12))
        self.label_show_path.pack()
        
        self.btn_connect = ctk.CTkButton(self.frame_1, text=f"{' Connect to ETABS ':#^70s}", command=self.connect_etabs, width=ui_width, font=('consolas',18))
        self.btn_connect.pack(pady=5)

        #### Frame-2
        ##### Frame 2-1
        self.frame_2_1 = ctk.CTkFrame(self.frame_2, width=ui_width/3)
        self.frame_2_1.grid(row=0, column=0)
        ##### Frame-2-1-1
        self.label_2_1_1 = ctk.CTkLabel(self.frame_2_1, text='Fast Release', anchor='w',font=('consolas',16))
        self.label_2_1_1.pack(anchor='w')
        self.frame_2_1_1 = ctk.CTkFrame(self.frame_2_1)
        self.frame_2_1_1.pack()

        self.btn_release_i = ctk.CTkButton(self.frame_2_1_1, text="Release I", command=self.release_i, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_i.grid(row=0, column=0, padx=0, pady=5)
        self.btn_release_j = ctk.CTkButton(self.frame_2_1_1, text="Release J", command=self.release_j, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_j.grid(row=1, column=0, padx=0, pady=5)
        self.btn_release_ij = ctk.CTkButton(self.frame_2_1_1, text="Release IJ", command=self.release_ij, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_ij.grid(row=2, column=0, padx=0, pady=5)

        ##### Frame-2-1-2
        self.label_2_1_2 = ctk.CTkLabel(self.frame_2_1, text='\nAlways Do those', anchor='w', font=('consolas',16))
        self.label_2_1_2.pack(anchor='w')
        self.frame_2_1_2 = ctk.CTkFrame(self.frame_2_1)
        self.frame_2_1_2.pack()        

        self.btn_reduJ = ctk.CTkButton(self.frame_2_1_2, text="Torsion Reduction", command=self.reduction_torsion, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_reduJ.grid(row=0, column=0, padx=0, pady=5)
        self.btn_set_rz = ctk.CTkButton(self.frame_2_1_2, text="Set Rigidzone", command=self.set_rz, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_set_rz.grid(row=1, column=0, padx=0, pady=5)
        self.btn_sb_nonsway = ctk.CTkButton(self.frame_2_1_2, text="SB,FB Nonsway", command=self.sb_nonsway, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_sb_nonsway.grid(row=2, column=0, padx=0, pady=5)

        ##### Frame 2-2
        self.frame_2_2 = ctk.CTkFrame(self.frame_2, width=ui_width/3)
        self.frame_2_2.grid(row=0, column=1)

        ##### Frame 2-3
        self.frame_2_3 = ctk.CTkFrame(self.frame_2, width=ui_width/3)
        self.frame_2_3.grid(row=0, column=2)

        self.btn_loading = ctk.CTkButton(self.frame_2_3, text="Click Me to Loading", command=self.open_loading, width=ui_width/3, font=('consolas',12))
        self.btn_loading.grid(row=3, column=0, padx=0, pady=5)

        #### Frame 3
        self.label_tb = ctk.CTkLabel(self.frame_3, width = ui_width, text = 'Messagebox', anchor='w',font=('consolas',16))
        self.label_tb.pack()
        self.tb = ctk.CTkTextbox(self.frame_3, width=ui_width, font=('consolas',12))
        self.tb.pack(padx=5)
        sys.stdout = self # To show print messages
        sys.stderr = self # To show error messages

        self.Loading = None

        self.app.mainloop()
    
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

