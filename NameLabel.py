# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:28:38 2019

@author: Justin Corcuera
"""

from tkinter import * 

class NameLabel():
    
    def __init__(self, root):
        self.label = Label(root, text = "Fate Summoner",
                      justify = "center", bg = "#CBCACA",
                      font = ("Times", 14, "bold"), borderwidth = 1,
                      relief = "raised")
        
        self.label.place(height = 30, width = 250, x = 35, y = 376)
        
    def change_text(self, name):
        self.label.config(text = name)