# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:54:40 2019

@author: Justin Corcuera
"""
from tkinter import * 

class OptionMenu():
    
    def __init__(self, menu, root):
        option_menu = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "Options", menu = option_menu)
        
        option_menu.add_command(label = "Edit Configuration", command = self.edit)
        option_menu.add_separator()
        option_menu.add_command(label = "Exit",command = root.destroy)
        
    def edit(self):         #TODO: Consider cutting this entirely, but also consider making a button the resets the config back to all servants unclaimed.
        self.popupmsg()
    
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
    