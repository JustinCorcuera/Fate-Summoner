# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:28:38 2019

@author: Justin Corcuera
"""

from tkinter import * 

class NameLabel():
    
    def __init__(self, root):
        self.label = Label(root, text = "Jeanne Spam Alter Spam Santa Spam Lily",
                      justify = "center", bg = "#CBCACA",
                      font = ("Times", 24, "bold"), borderwidth = 1,
                      relief = "raised")
        
        self.label.place(height = 50, width = 760, x = 20, y = 10)
        
    def change_text(self, name):
        self.label.config(text = name)