# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:00:33 2019

@author: Justin Corcuera
"""

from tkinter import * 

class LineLabel():
    
    def __init__(self, root):
        self.label = Label(root, text = "I'm Jeanne! It's a bit early for Christmas but, let's do our best together! By the way, do you know how this Sled moves?",
                      justify = "center", bg = "#CBCACA",
                      font = ("Times", 12, "bold"), borderwidth = 1,
                      wraplength = 500,
                      relief = "raised")
        
        self.label.place(height = 160, width = 760, x = 20, y = 430)
        
    def change_text(self, name):
        print("TODO: Changxe label text to new Servant name.")
        self.label.config(text = name)