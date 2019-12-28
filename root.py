# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:46:49 2019

@author: Justin Corcuera
"""

from tkinter import * 
from OptionMenu import OptionMenu
from NameLabel import NameLabel
from PictureLabel import PictureLabel
from LineLabel import LineLabel
from ClassLabel import ClassLabel
from ClaimButton import ClaimButton
from SummonButton import SummonButton
from ConfigUtility import ConfigUtility
from pathlib import Path
from PIL import Image
import PIL.ImageTk

#Create the main frame
root = Tk()
root.geometry('630x575')
root.resizable(False, False)    

#setting background
file_path = Path("GraphicAssets/background.png")        
        
image = Image.open(file_path)
image = image.resize((630, 575), Image.ANTIALIAS)
picture = PIL.ImageTk.PhotoImage(image)
        
background = Label(image = picture)
background.image = picture #deals with weird Tkinter garbage collection

background.place(height = 575, width = 630, x = 0, y = 0)
                 
#Creating the menu bar and the option menu
menu = Menu()
root.config(menu = menu)
option_menu = OptionMenu(menu, root)

#Creating the Servant image label
picture = PictureLabel(root)

#Creating the Servant name label
name = NameLabel(root)

#Creating the Servant class label
servant_class = ClassLabel(root)

#Creating the Servant summoning line label
line = LineLabel(root)

#Creating the Claim button
claim_button = ClaimButton(root)


#Creating the Summon Button
summon_button = SummonButton(root, name, picture, servant_class, line, claim_button)

#mainloop
root.mainloop()