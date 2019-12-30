# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:00:33 2019

@author: Justin Corcuera
"""

from tkinter import * 
from pathlib import Path
from PIL import Image
import PIL.ImageTk

class LineLabel():
    
    def __init__(self, root):
        
        
        file_path = Path("GraphicAssets/LineBG.png")  
        
        image = Image.open(file_path)
        image = image.resize((600, 130), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(root, text = "",
                      justify = "center", image = picture,
                      font = ("Source Sans Pro", 10, "bold"), borderwidth = 1,
                      wraplength = 590, fg = "white",
                      compound = CENTER)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        self.label.place(height = 130, width = 600, x = 15, y = 430)
        
    def change_text(self, line):
        self.label.config(text = line)