import customtkinter as ctk
from yc_etabs_api.etabs import ETABS
from show_msg import *

def connect_etabs(self) :
    msg = 'Connect Button'
    click_msg(msg)

    if self.etabs == None :
            etabs = ETABS()
            self.etabs = etabs
            self.btn_connect.configure(text = f'Connected to {self.etabs.EDB_name}!!')
            self.label_show_path.configure(text = f'Path is {self.etabs.EDB_path}')

    else :
        self.btn_connect.configure(text = f"Disconnect to {self.etabs.EDB_name}!! Click to connect again !! ")
        self.etabs = None

        self.label_show_path.configure(text = '')
        
    done_msg(msg)

    return self

def release_i(self) :
    msg = 'Release I-End'
    click_msg(msg)

    self.etabs.model_unlock()

    selected_frames = self.etabs.Select.get(type_='Frame')

    for frame in selected_frames :
        self.etabs.Frames.set_release(frame, quick='Mi')

    self.etabs.refresh()

    done_msg(msg)

    return self

def release_j(self) :
    msg = 'Release J-End'
    click_msg(msg)

    self.etabs.model_unlock()

    selected_frames = self.etabs.Select.get(type_='Frame')

    for frame in selected_frames :
        self.etabs.Frames.set_release(frame, quick='Mj')

    self.etabs.refresh()
    
    done_msg(msg)

    return self

def release_ij(self) :
    msg = 'Release Both-End'
    click_msg(msg)

    self.etabs.model_unlock()

    selected_frames = self.etabs.Select.get(type_='Frame')

    for frame in selected_frames :
        self.etabs.Frames.set_release(frame, quick='Mij')

    self.etabs.refresh()
    
    done_msg(msg)

    return self

def reduction_torsion(self, reduction = 0.1) : # need to test
    msg = 'Torsion Constant Reduction'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list(by_unique = False)
    
    for frame, story in frames :
        if frame[0] == 'B' :
            self.etabs.Frame.set_modifier(frame, T = reduction)
    
    self.etabs.refresh()
    
    done_msg(msg)
    
    return self

def set_rz(self, rz = 0.5, frame_prefix = ['B', 'C', 'D']) : # need to test
    msg = 'Set Rigidzone'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list()
    
    for frame in frames :
        if self.etabs.Frames.get_section(frame)[0] in frame_prefix :
            self.etabs.set_rigidzone(frame, rz)
        else :
            self.etabs.set_rigidzone(frame, 0.0)
    
    done_msg(msg)
    
    return self

def sb_nonsway(self, frame_prefix = ['F', 'S']) : # need to test
    msg = 'SBeam and FBeam Nonsway'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list()
    
    for frame in frames :
        if self.etabs.Frames.get_section(frame)[0] in frame_prefix :
            self.etabs.Design.ConcFrame.set_overwrite('', 0, 0, quick = 'nonsway')
        else :
            self.etabs.Design.ConcFrame.set_overwrite('', 0, 0, quick = 'sway')
    
    done_msg(msg)
    
    return self

if __name__ == '__main__' :
    etabs = ETABS()