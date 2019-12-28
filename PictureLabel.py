# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:11:54 2019

@author: Justin Corcuera
"""

from tkinter import * 
from pathlib import Path
from PIL import Image
import PIL.ImageTk

class PictureLabel():
    
    def __init__(self, root):
        
        file_path = Path("ServantArt/test.png")        
        
        image = Image.open(file_path)
        image = image.resize((300, 350), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(borderwidth = 1, relief = "raised", image = picture)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        self.label.place(height = 350, width = 300, x = 250, y = 70)
        
    def change_pic(self, pic):
        
        file_path = Path("ServantArt/" + pic)
        
        image = Image.open(file_path)
        image = image.resize((300, 350), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label.configure(image = picture)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.html