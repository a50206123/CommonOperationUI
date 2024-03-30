import customtkinter as ctk
from yc_etabs_api.etabs import ETABS
import cmd_loading as cmd

class LoadingUI :
    def __init__(self, etabs:ETABS) -> None:
        self.etabs = etabs

        self.initUI()
        
        self.app.mainloop()

    def initUI(self) :
        ctk.set_appearance_mode('dark') 
        # ctk.set_default_color_theme()

        app = ctk.CTk()
        app.geometry('1200x600')
        app.title('ETABS Loading Faster by YuChen Lin')

        label_story_height = ctk.CTkLabel(app, text='Story Height : (m)')
        entry_story_height = ctk.CTkEntry(app)
        label_story_height.grid(row = 0, column = 0, padx = 5, pady = 5)
        entry_story_height.grid(row = 0, column = 1, pady = 5)

        label_beam_depth = ctk.CTkLabel(app, text='The depth of beam : (m)')
        entry_beam_depth = ctk.CTkEntry(app)
        label_beam_depth.grid(row = 0, column = 2, padx = 5, pady = 5)
        entry_beam_depth.grid(row = 0, column = 3, pady = 5)

        btn_calc = ctk.CTkButton(app, text='Calculating', width = 300, command=self.calc_load)
        btn_calc.grid(row = 0, column = 4, columnspan = 2, pady = 5)

        label_t_rc = ctk.CTkLabel(app, text='Thickness of RC Wall : (cm)')
        entry_t_rc = ctk.CTkEntry(app)
        label_t_rc.grid(row = 1, column = 0, padx = 5, pady = 5)
        entry_t_rc.grid(row = 1, column = 1, pady = 5)

        label_t_ot = ctk.CTkLabel(app, text='Thickness of OTHER Wall : (cm)')
        entry_t_ot = ctk.CTkEntry(app)
        label_t_ot.grid(row = 1, column = 2, padx = 5, pady = 5)
        entry_t_ot.grid(row = 1, column = 3, pady = 5)
        label_w_ot = ctk.CTkLabel(app, text='Unit Weight of OTHER Wall : (tf/m3)')
        entry_w_ot = ctk.CTkEntry(app)
        label_w_ot.grid(row = 1, column = 4, padx = 5, pady = 5)
        entry_w_ot.grid(row = 1, column = 5, pady = 5)
        

        self.app = app
        self.label_story_height = label_story_height
        self.entry_story_height = entry_story_height
        self.label_beam_depth = label_beam_depth
        self.entry_beam_depth = entry_beam_depth
        self.label_t_rc = label_t_rc
        self.entry_t_rc = entry_t_rc
        self.label_t_ot = label_t_ot
        self.entry_t_ot = entry_t_ot
        self.label_w_ot = label_w_ot
        self.entry_w_ot = entry_w_ot
        self.btn_loading = []
    
    def calc_load(self) :
        cmd.calc_loading(self)
        
    def add_loading(self) :
        cmd.add_loading(self)

if __name__ == '__main__' : 
    pass