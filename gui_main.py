import sys
from typing import Any, Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk
from yc_etabs_api.etabs import ETABS
from gui_loading import LoadingUI
# from cmd_section import SectionUI

import threading 

from show_msg import *

ui_width = 621

etabs = None

import cmd_main as cmd

class CommonOperationUI(ctk.CTk) :
    def __init__(self) -> None:
        super().__init__()

        # self.etabs = None

        self.initUI()

    
    def initUI(self) :
        ctk.set_appearance_mode('dark') 
        ctk.set_default_color_theme("gui_theme.json")
        ctk.FontManager.load_font('consola.ttf')

        self.geometry('640x480')
        self.title('ETABS Faster by YuChen Lin')

        self.frame_etabs_connect = FrameEtabsConnect(self, width=ui_width)
        self.frame_etabs_connect.pack()
        self.frame_func = ctk.CTkFrame(self, width=ui_width)
        self.frame_func.pack()
        self.frame_3 = ctk.CTkFrame(self)
        self.frame_3.pack()

        #### Frame-2
        ##### Frame 2-1
        self.frame_common_operation = FrameCommonOperation(self.frame_func, width=ui_width/3)
        self.frame_common_operation.grid(row=0, column=0)

        ##### Frame 2-2
        self.frame_2_2 = ctk.CTkFrame(self.frame_func, width=ui_width/3)
        self.frame_2_2.grid(row=0, column=1)

        self.label_2_2 = ctk.CTkLabel(self.frame_2_2, width = ui_width/3, text = 'Automatic Programs')
        self.label_2_2.pack(pady = 5, anchor='n')

        self.btn_change_section = ctk.CTkButton(self.frame_2_2, text="Change Sections", command=self.change_section, width=ui_width/3, font=('consolas',12))
        self.btn_change_section.pack(padx=0, pady=5)
        

        ##### Frame 2-3
        self.frame_2_3 = ctk.CTkFrame(self.frame_func, width=ui_width/3)
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

        self.mainloop()

    # Callback function for text
    def write(self, txt) :
        threading.Thread(target=self.tb.insert(tk.END, txt)).start()     
        self.tb.see(tk.END)
    
    @tic_toc('Release I-End') 
    def release_i(self) :
        self = cmd.release_i(self)

    @tic_toc('Release J-End') 
    def release_j(self) :
        self = cmd.release_j(self)

    @tic_toc('Release Both-End') 
    def release_ij(self) :
        self = cmd.release_ij(self)

    @tic_toc('Torsion Reduction') 
    def reduction_torsion(self) :
        self = cmd.reduction_torsion(self)

    @tic_toc('Select Frames with Rigidzone = 0.5') 
    def set_rz(self) :
        self = cmd.set_rz(self)
    
    @tic_toc('FBeam/SBeam Nonsway Overwrite') 
    def sb_nonsway(self) :
        self = cmd.sb_nonsway(self)

    @tic_toc('Opening Loading Window') 
    def open_loading(self) :
        self.Loading = LoadingUI(self.etabs)

    @tic_toc('Changing Section')
    def change_section(self) :
        self = cmd.change_section(self)

class FrameEtabsConnect(ctk.CTkFrame) :
    def __init__(self, master, width: int = 200, height: int = 200):
        super().__init__(master, width, height)

        self.master = master

        self.label_show_path = ctk.CTkLabel(self, text=" ", width=ui_width, font=('consolas',12))
        self.label_show_path.pack()
        
        self.btn_connect = ctk.CTkButton(self, text=f"{' Connect to ETABS ':#^70s}", command=self.connect_etabs, width=ui_width, font=('consolas',18))
        self.btn_connect.pack(pady=5)

    @tic_toc('Connect ETABS') 
    def connect_etabs(self) :
        global etabs 

        if etabs == None :
            etabs = ETABS()
            self.btn_connect.configure(text = f"{f' Connected to {etabs.EDB_name}!! ':#^70s}")
            self.label_show_path.configure(text = f'Path : {etabs.EDB_path}')

        else :
            self.btn_connect.configure(text = f'{f" Disconnect to EABS!! ":#^70s}')
            self.etabs = None

            self.label_show_path.configure(text = ' ')

class FrameCommonOperation(ctk.CTkFrame) :
    def __init__(self, master, width: int = 200, height: int = 200):
        super().__init__(master, width, height)

        self.frame = ctk.CTkFrame(self, width=ui_width/3)
        self.frame.grid(row=0, column=0)
        ##### Frame-2-1-1
        self.label_1 = ctk.CTkLabel(self.frame, text='Fast Release', anchor='w',font=('consolas',16))
        self.label_1.pack(anchor='w')
        self.frame_1 = ctk.CTkFrame(self.frame)
        self.frame_1.pack()

        self.btn_release_i = ctk.CTkButton(self.frame_1, text="Release I", command=self.release_i, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_i.grid(row=0, column=0, padx=0, pady=5)
        self.btn_release_j = ctk.CTkButton(self.frame_1, text="Release J", command=self.release_j, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_j.grid(row=1, column=0, padx=0, pady=5)
        self.btn_release_ij = ctk.CTkButton(self.frame_1, text="Release IJ", command=self.release_ij, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_release_ij.grid(row=2, column=0, padx=0, pady=5)

        ##### Frame-2-1-2
        self.label_2 = ctk.CTkLabel(self.frame, text='\nAlways Do those', anchor='w', font=('consolas',16))
        self.label_2.pack(anchor='w')
        self.frame_2 = ctk.CTkFrame(self.frame)
        self.frame_2.pack()        

        self.btn_reduJ = ctk.CTkButton(self.frame_2, text="Torsion Reduction", command=self.reduction_torsion, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_reduJ.grid(row=0, column=0, padx=0, pady=5)
        self.btn_set_rz = ctk.CTkButton(self.frame_2, text="Select Rigidzone = 0.5", command=self.set_rz, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_set_rz.grid(row=1, column=0, padx=0, pady=5)
        self.btn_sb_nonsway = ctk.CTkButton(self.frame_2, text="SB,FB Nonsway", command=self.sb_nonsway, height = 20, width=ui_width/3, font=('consolas',12))
        self.btn_sb_nonsway.grid(row=2, column=0, padx=0, pady=5)
    
    @tic_toc('Release I-End') 
    def release_i(self) :
        global etabs

        etabs.model_unlock()

        selected_frames = etabs.Select.get(type_='Frame')

        for frame in selected_frames :
            etabs.Frames.set_release(frame, quick='Mi')

        etabs.refresh()

    @tic_toc('Release J-End') 
    def release_j(self) :
        global etabs

        etabs.model_unlock()

        selected_frames = etabs.Select.get(type_='Frame')

        for frame in selected_frames :
            etabs.Frames.set_release(frame, quick='Mj')

        etabs.refresh()

    @tic_toc('Release Both-End') 
    def release_ij(self) :
        global etabs 

        etabs.model_unlock()

        selected_frames = etabs.Select.get(type_='Frame')

        for frame in selected_frames :
            etabs.Frames.set_release(frame, quick='Mij')

        etabs.refresh()
        

    @tic_toc('Torsion Reduction') 
    def reduction_torsion(self, reduction = 0.1) :
        global etabs

        etabs.model_unlock()
        
        frames = etabs.Frames.get_name_list(by_unique = False)
        
        for frame, story  in frames :
            unique = etabs.Frames.label2unique(story, frame)
            J_orig = etabs.Frames.get_modifier(unique)[3]

            if frame[0] == 'B' and J_orig != reduction :
                etabs.Frames.set_modifier(unique, T = reduction)
        
        etabs.refresh()

    @tic_toc('Select Frames with Rigidzone = 0.5') 
    def set_rz(self, rz = 0.5, frame_prefix = ['B', 'C', 'D']) : # Just Selected frames which need to assign rigidzone
        global etabs

        etabs.model_unlock()
        
        frames = etabs.Frames.get_name_list()

        for frame in frames :
            rz_orig = etabs.Frames.get_rigidzone(frame)
            sect = etabs.Frames.get_section(frame)

            if (sect[0] in frame_prefix) and (rz_orig != rz):
                etabs.Frames.set_selected(frame)
                # self.etabs.Frames.set_rigidzone(frame, rz)
            elif not (sect[0] in frame_prefix) and (rz_orig != 0.0):
                # self.etabs.Frames.set_rigidzone(frame, 0.0)
                pass
        
        etabs.refresh()
    
    @tic_toc('FBeam/SBeam Nonsway Overwrite') 
    def sb_nonsway(self, frame_prefix = ['F', 'S']) :
        global etabs

        etabs.model_unlock()
        
        frames = etabs.Frames.get_name_list(by_unique = False)
        
        for frame, story in frames :
            if etabs.Define.Material.get(etabs.Frames.get_section(frame))['mat_type'] != 2 :
                # Not Concrete then SKIP
                continue

            unique = etabs.Frames.label2unique(story, frame)
            frame_type = etabs.Design.ConcFrame.get_overwrite(unique, 0, quick = 'frame type')
            sect = etabs.Frames.get_section(unique)

            if (sect[0] in frame_prefix) and (frame_type != 'nonsway') :
                etabs.Design.ConcFrame.set_overwrite(unique, 0, 0, quick = 'nonsway')
            elif not (sect[0] in frame_prefix) and (frame_type != 'sway') :
                etabs.Design.ConcFrame.set_overwrite(unique, 0, 0, quick = 'sway')
        
        etabs.refresh()

class FrameAutomatic(ctk.CTkFrame) :
    def __init__(self, master: Any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)

        
if __name__ == '__main__' :
    app = CommonOperationUI()

