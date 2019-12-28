# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:00:33 2019

@author: Justin Corcuera
"""

from tkinter import * 

class LineLabel():
    
    def __init__(self, root):
        self.label = Label(root, text = "",
                      justify = "center", bg = "#CBCACA",
                      font = ("Times", 12, "bold"), borderwidth = 1,
                      wraplength = 500,
                      relief = "raised")
        
        self.label.place(height = 130, width = 600, x = 15, y = 430)
        
    def change_text(self, line):
        self.label.config(text = line)