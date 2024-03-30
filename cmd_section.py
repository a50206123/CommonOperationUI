import customtkinter as ctk
from yc_etabs_api.etabs import ETABS
from show_msg import *

def auto_add_section_definition(self) :
    msg = 'Auto Adding Sectional Definitions'
    click_msg(msg)
    
    done_msg(msg)
    return self

def auto_change_mat_by_story(self) :
    msg = 'Auto Changing Sectional Material by Stories'
    click_msg(msg)
    
    done_msg(msg)
    return self

def auto_try_section(self) :
    msg = 'Auto Trying Beam and Column Section'
    click_msg(msg)
    
    done_msg(msg)
    return self