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
        option_menu.add_command(label = "Load Configuration", command = self.load)
        option_menu.add_command(label = "Save As", command = self.save)
        option_menu.add_separator()
        option_menu.add_command(label = "Exit",command = root.destroy)
        
    def edit(self):
        print("Edit")
        
    def load(self):
        print("Load")
        
    def save(self):
        print("Save")