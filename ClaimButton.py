# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:45:33 2019

@author: Justin Corcuera
"""

from tkinter import * 
from ConfigUtility import ConfigUtility
from pathlib import Path
from PIL import Image
import PIL.ImageTk

servant = ""
util = None

class ClaimButton():
        
    def __init__(self, root):
        
#        Creating background Label
#        self.label = Label(borderwidth = 1, relief = "raised", bg = "#CBCACA")      
#        self.label.place(height = 70, width = 160, x = 440, y = 120)
        
        file_path = Path("GraphicAssets/Button.png")  
        
        image = Image.open(file_path)
        image = image.resize((140, 60), Image.ANTIALIAS)
        picture = PIL.ImageTk.PhotoImage(image)
        
        #Creating Claim Button
        self.button = Button(root, text = "Claim", font = ("Verdana", 18, "bold"), 
                             image = picture, fg = "#0E2460", compound = CENTER, 
                             command = lambda: self.claim())
        self.button.image = picture #deals with wierd Tkinter garbage collection
        
        self.button.place(height = 60, width = 140, x = 398, y = 240)
        #23
    def current_name(self, name, utility):
        global servant
        global util
        
        #sets current Servant and current instance of the ConfigUtility   
        util = utility
        servant = name

    def claim(self):
        global servant
        claim_dict = util.claimed()
        
        if servant != "":  
            claim_dict[servant] = True
            util.update_config_claim(servant)