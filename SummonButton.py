# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 00:02:16 2019

@author: ramenblitz
"""

from tkinter import * 

class SummonButton():
    
    def __init__(self, root):
        
        #Creating background Label
        self.label = Label(borderwidth = 1, relief = "raised", bg = "#CBCACA")      
        self.label.place(height = 70, width = 160, x = 590, y = 320)
        
        #Creating Claim Button
        self.button = Button(root, text = "Summon")
        self.button.place(height = 50, width = 140, x = 600, y = 330)
        