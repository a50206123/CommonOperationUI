import customtkinter as ctk
from yc_etabs_api.etabs import ETABS
from show_msg import *

def connect_etabs(self) :
    msg = 'Connect Button'
    click_msg(msg)

    if self.etabs == None :
            etabs = ETABS()
            self.etabs = etabs
            self.btn_connect.configure(text = f"{f' Connected to {self.etabs.EDB_name}!! ':#^70s}")
            self.label_show_path.configure(text = f'Path : {self.etabs.EDB_path}')

    else :
        self.btn_connect.configure(text = f'{f" Disconnect to EABS!! ":#^70s}')
        self.etabs = None

        self.label_show_path.configure(text = ' ')
        
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

def reduction_torsion(self, reduction = 0.1) : # OK
    msg = 'Torsion Constant Reduction'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list(by_unique = False)
    
    for frame, story  in frames :
        unique = self.etabs.Frames.label2unique(story, frame)
        J_orig = self.etabs.Frames.get_modifier(unique)[3]

        if frame[0] == 'B' and J_orig != reduction :
            self.etabs.Frames.set_modifier(unique, T = reduction)
    
    self.etabs.refresh()
    
    done_msg(msg)
    
    return self

def set_rz(self, rz = 0.5, frame_prefix = ['B', 'C', 'D']) : # Just Selected frames which need to assign rigidzone
    msg = 'Set Rigidzone'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list()

    for frame in frames :
        rz_orig = self.etabs.Frames.get_rigidzone(frame)
        sect = self.etabs.Frames.get_section(frame)

        if (sect[0] in frame_prefix) and (rz_orig != rz):
            self.etabs.Frames.set_selected(frame)
            # self.etabs.Frames.set_rigidzone(frame, rz)
        elif not (sect[0] in frame_prefix) and (rz_orig != 0.0):
            # self.etabs.Frames.set_rigidzone(frame, 0.0)
            pass
    
    self.etabs.refresh()
    
    done_msg(msg)
    
    return self

def sb_nonsway(self, frame_prefix = ['F', 'S']) : # OK
    msg = 'SBeam and FBeam Nonsway'
    click_msg(msg)
    
    self.etabs.model_unlock()
    
    frames = self.etabs.Frames.get_name_list(by_unique = False)
    
    for frame, story in frames :
        unique = self.etabs.Frames.label2unique(story, frame)
        frame_type = self.etabs.Design.ConcFrame.get_overwrite(unique, 0, quick = 'frame type')
        sect = self.etabs.Frames.get_section(unique)

        if (sect[0] in frame_prefix) and (frame_type != 'nonsway') :
            self.etabs.Design.ConcFrame.set_overwrite(unique, 0, 0, quick = 'nonsway')
        elif not (sect[0] in frame_prefix) and (frame_type != 'sway') :
            self.etabs.Design.ConcFrame.set_overwrite(unique, 0, 0, quick = 'sway')
    
    self.etabs.refresh()
    
    done_msg(msg)
    
    return self

if __name__ == '__main__' :
    etabs = ETABS()