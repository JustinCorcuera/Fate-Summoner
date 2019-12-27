# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:45:33 2019

@author: ramenblitz
"""

from tkinter import * 

class ClaimButton():
    
    def __init__(self, root):
        
        #Creating background Label
        self.label = Label(borderwidth = 1, relief = "raised", bg = "#CBCACA")      
        self.label.place(height = 70, width = 160, x = 50, y = 320)
        
        #Creating Claim Button
        self.button = Button(root, text = "Claim")
        self.button.place(height = 50, width = 140, x = 60, y = 330)
        