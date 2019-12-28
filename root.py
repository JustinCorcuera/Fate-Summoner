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

#Create the main frame
root = Tk()
root.geometry('800x600')
root.resizable(False, False)

#Creating the menu bar and the option menu
menu = Menu()
root.config(menu = menu)
option_menu = OptionMenu(menu, root)

#Creating the Servant name label
name = NameLabel(root)

#Creating the Servant image label
picture = PictureLabel(root)

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