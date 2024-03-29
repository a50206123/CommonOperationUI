import customtkinter as ctk
from yc_etabs_api.etabs import ETABS

class LoadingUI :
    def __init__(self, etabs:ETABS) -> None:

        self.etabs = etabs

        ctk.set_appearance_mode('dark') 
        # ctk.set_default_color_theme()

        app = ctk.CTk()
        app.geometry('1200x600')
        app.title('Loading Helper ft. TedChu')

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

        app.mainloop()

    def calc_load(self) :
        story_height = float(self.entry_story_height.get())
        beam_depth = float(self.entry_beam_depth.get())
        try :
            t_rc = float(self.entry_t_rc.get())/100
            w_rc = 2.4
            haveRC = True
        except :
            haveRC = False

        try :
            t_ot = float(self.entry_t_ot.get())/100
            w_ot = float(self.entry_w_ot.get())
            haveOT = True
        except : 
            haveOT = False

        clear_height = story_height - beam_depth

        line_loading = lambda w, h, t : w * h * t

        btn_loading_rc = []
        btn_loading_ot = []
        commands = []

        for i in range(4) :
            if haveRC :
                tmp1 = ctk.CTkButton(self.app, text = f'RC {(i+1)*25}%-{line_loading(w_rc, clear_height, t_rc)*(i+1)*0.25:.3f}')
                tmp1.grid(row = 5- i, column = 0, pady = 10)
                btn_loading_rc.append(tmp1)
            
            if haveOT :
                tmp2 = ctk.CTkButton(self.app, text = f'Other {(i+1)*25}%-{line_loading(w_ot, clear_height, t_ot)*(i+1)*0.25:.3f}')
                tmp2.grid(row =  5- i, column = 1, pady = 10)
                btn_loading_ot.append(tmp2)


        self.btn_loading_rc = btn_loading_rc
        self.btn_loading_ot = btn_loading_ot

if __name__ == '__main__' : 
    pass