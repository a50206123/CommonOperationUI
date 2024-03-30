import customtkinter as ctk
from yc_etabs_api.etabs import ETABS
from show_msg import *

def calc_loading(self) :
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
    commands_rc = []
    commands_ot = []
    line_load_rc = line_loading(w_rc, clear_height, t_rc)
    line_load_ot = line_loading(w_ot, clear_height, t_ot)
    for i in range(4) :
        if haveRC :
            tmp1 = ctk.CTkButton(self.app, text = f'RC {(i+1)*25}%-{line_load_rc*(i+1)*0.25:.3f}', command=lambda: add_loading(line_load_rc*(i+1)*0.25))
            tmp1.grid(row = 5- i, column = 0, pady = 10)
            btn_loading_rc.append(tmp1)
        
        if haveOT :
            tmp2 = ctk.CTkButton(self.app, text = f'Other {(i+1)*25}%-{line_load_ot*(i+1)*0.25:.3f}', command=lambda: add_loading(line_load_ot*(i+1)*0.25))
            tmp2.grid(row =  5- i, column = 1, pady = 10)
            btn_loading_ot.append(tmp2)


    self.btn_loading_rc = btn_loading_rc
    self.btn_loading_ot = btn_loading_ot

def add_loading(self, loading:float, is_replace = False) :
    msg = f'Add Line Load ({loading:.3f}tf/m)'
    click_msg(msg)

    self.etabs.model_unlock()

    selected_frames = self.etabs.Select.get(type_='Frame')

    for frame in selected_frames :
        self.etabs.Frames.assign_load(frame, "DEAD", loading)

    self.etabs.refresh()

    done_msg(msg)

def add_point_load(self) :
    pass

def add_line_load(self) :
    pass

def add_area_load(self) :
    pass