# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:28:38 2019

@author: Justin Corcuera
"""

from tkinter import * 
from pathlib import Path
from PIL import Image
import PIL.ImageTk

class NameLabel():
    
    def __init__(self, root):
        
        file_path = Path("GraphicAssets/NameBG.png")  
        
        image = Image.open(file_path)
        image = image.resize((250, 30), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(root, text = "Fate Summoner",
                      justify = "center", fg = "#0F2E80",
                      font = ("Source Sans Pro", 10, "bold"), borderwidth = 1,
                      image = picture, compound = CENTER)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        self.label.place(height = 30, width = 250, x = 35, y = 376)
        
    def change_text(self, name):
        self.label.config(text = name)