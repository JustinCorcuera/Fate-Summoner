# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:29:24 2019

@author: Justin Corcuera
"""

from tkinter import * 
from pathlib import Path
from PIL import Image
import PIL.ImageTk

class ClassLabel():
    
    def __init__(self, root):
        
        file_path = Path("ClassIcon/Lancer.png")
        
        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(borderwidth = 1, relief = "raised", image = picture, bg = "#CBCACA")
        self.label.image = picture #deals with wierd Tkinter garbage collection
        
        self.label.place(height = 100, width = 100, x = 80, y = 70)
        
    def change_class(self, pic):
        
        file_path = Path("ClassIcon/" + pic)
        
        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label.configure(image = picture)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.html