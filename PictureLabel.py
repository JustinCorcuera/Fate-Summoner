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
        self.label.image = picture #deals with wierd Tkinter garbage collection
        
        self.label.place(height = 350, width = 300, x = 250, y = 70)
        
    def change_pic(self, picture):
        print("TODO: Change label pic to new Servant picture.")
        #self.label.config(text = name)
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm