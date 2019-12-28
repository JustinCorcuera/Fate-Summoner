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
        
        #Creating background Label
        file_path = Path("GraphicAssets/PictureBG.png")        
        
        imagebg = Image.open(file_path)
        imagebg = imagebg.resize((290, 406), Image.ANTIALIAS)
        picturebg = PIL.ImageTk.PhotoImage(imagebg)
        
        self.back = Label(image = picturebg)  
        self.back.image = picturebg #deals with weird Tkinter garbage collection
        
        self.back.place(height = 406, width = 290, x = 15, y = 15)
        
        file_path = Path("ServantArt/default.jpg")        
        
        image = Image.open(file_path)
        image = image.resize((280, 396), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label = Label(image = picture)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        self.label.place(height = 396, width = 280, x = 20, y = 20)
        
        
    def change_pic(self, pic):
        
        file_path = Path("ServantArt/" + pic)
        
        image = Image.open(file_path)
        image = image.resize((280, 396), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        self.label.configure(image = picture)
        self.label.image = picture #deals with weird Tkinter garbage collection
        
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.html