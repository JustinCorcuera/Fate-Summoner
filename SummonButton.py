# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 00:02:16 2019

@author: Justin Corcuera
"""

from tkinter import * 
from ConfigUtility import ConfigUtility
from PictureLabel import PictureLabel
from NameLabel import NameLabel
from LineLabel import LineLabel
from ClassLabel import ClassLabel

class SummonButton():
    
    def __init__(self, root, name, picture, servant_class, line, claim):
        
#        Creating background Label
#        self.label = Label(borderwidth = 1, relief = "raised", bg = "#CBCACA")      
#        self.label.place(height = 70, width = 160, x = 440, y = 320)
        
        #Creating Claim Button
        self.button = Button(root, text = "Summon", command = lambda: self.summon(name, picture, servant_class, line, claim))
        self.button.place(height = 50, width = 140, x = 450, y = 240)
        
    def summon(self ,name, picture, servant_class, line, claim):
        #initialize ConfigUtility
        util = ConfigUtility()
        
        claimed = util.claimed()
        pic_url = util.pic_dict()
        lines = util.line_dict()
        classes = util.class_dict()
        claim_status = util.get_claim_status()
        
        #Checks if all servants are claimed to stop infinite loop
        if not False in claim_status:
            print("test")       #TODO: Set logic for no more Servants to Claim
            
        else:
            
            #checks if the Servant name is able to be summoned.
            while True:
                servant = util.get_random()
                
                if claimed[servant] == False:
                    break
            
            #Changes the Name label to the new Servant
            name.change_text(servant)
            
            #Changes the line label to the new summoning line
            summon_line = lines[servant]
            line.change_text(summon_line)
            
            #Changes the picture to the new Servant's picture
            url = pic_url[servant]
            picture.change_pic(url)
            
            #Changes the class symbol to that of the new Servant
            class_url = classes[servant]
            servant_class.change_class(class_url)
            
            #Sets the current Servant to a variable in ClaimButton
            claim.current_name(servant, util)

        
        