# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:29:24 2019

@author: ramenblitz
"""

from tkinter import * 
from pathlib import Path
from PIL import Image
import PIL.ImageTk

class ClassLabel():
    
    def __init__(self, root):
        
        file_path = Path("ClassIcon/LancerGold.png")
        
        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(borderwidth = 1, relief = "raised", image = picture, bg = "#CBCACA")
        self.label.image = picture #deals with wierd Tkinter garbage collection
        
        self.label.place(height = 100, width = 100, x = 80, y = 70)
        
    def change_pic(self, picture):
        print("TODO: Change label pic to new Servant picture.")
        #self.label.config(text = name)
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm