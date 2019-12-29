# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:54:40 2019

@author: Justin Corcuera
"""
from tkinter import * 
from ConfigUtility import ConfigUtility

class OptionMenu():
    
    def __init__(self, menu, root):
        option_menu = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "Options", menu = option_menu)
        
        option_menu.add_command(label = "Reset Configuration", command = self.reset)
        option_menu.add_separator()
        option_menu.add_command(label = "Exit",command = root.destroy)
        
    def reset(self):         #TODO: Before calling reset_config, have a warning popup appear that confirms the option.
        util = ConfigUtility()
        
    
    def popupmsg(self):
        popup = Tk()
        popup.wm_title("Edit Configuration")
        popup.geometry('700x500')
        popup.resizable(False, False)

        label = Label(popup, text = "test")
        label.pack(side = "top", fill = "x", pady = 10)
        
        B1 = Button(popup, text = "Okay", command = popup.destroy)
        B1.pack()
        
        popup.mainloop()
    