## -*- coding: utf-8 -*-
#"""
#Created on Fri Dec 27 15:01:35 2019
#
#@author: Justin Corcuera
#"""

from tkinter import * 
import json
import random 

class ConfigUtility():
    
    def __init__(self):
        self.name_to_class = {}
        self.name_to_claim = {}
        self.name_to_pic = {}
        self.name_to_line = {}
        self.servants = []
        self.claim_status = []
        
        #Opens JSON config and assigns to variables. TODO:Change open and the file itself to .json
        with open('config.txt', 'r') as json_file:
            data = json.load(json_file)
            for p in data['Servant']:
                self.name = p['name']
                self.f_class = p['f_class']
                self.claim = p['claim']
                self.pic_url = p['pic_url']
                self.summon_line = p['line']
                self.name_to_class[self.name] = self.f_class
                self.name_to_claim[self.name] = self.claim
                self.name_to_pic[self.name] = self.pic_url
                self.name_to_line[self.name] = self.summon_line
                self.servants.append(p['name'])
                self.claim_status.append(p['claim'])  
            
    #Gets random Servant Name                
    def get_random(self):
        temp = []
        cntr = 0
        #Only randomly selects Servants that are not claimed in order to reduce potential roll time.
        for i in self.servants:
            if self.name_to_claim[i] == False:
                temp.append(self.servants[cntr])
                
            cntr += 1
        
        return self.servants[random.randint(0, len(temp) - 1)]
    
    #Gets list of all Servant names
    def get_all(self):
        return self.servants

    #Passes dict with names mapped to class
    def class_dict(self):
        return self.name_to_class
    
    #Passes dict with names mapped to claim status    
    def claimed(self):
        return self.name_to_claim

    #passes list with all claim statuses
    def get_claim_status(self):
        return self.claim_status

    #Passes dict with names mapped to pic url
    def pic_dict(self):
        return self.name_to_pic
    
    #Passes dict with names mapped to summoning lines
    def line_dict(self):
        return self.name_to_line
    
    #updates the configuration dict objects and JSON file
    def update_config_claim(self, servant):
        with open("config.txt", "r") as jsonFile:       

            data = json.load(jsonFile)      
            inp = servant                 

            for p in data['Servant']:       
                if(p['name'] == inp):         
                    p['claim'] = True  
                    
                self.name = p['name']
                self.f_class = p['f_class']
                self.claim = p['claim']
                self.pic_url = p['pic_url']
                self.summon_line = p['line']
                self.name_to_class[self.name] = self.f_class
                self.name_to_claim[self.name] = self.claim
                self.name_to_pic[self.name] = self.pic_url
                self.name_to_line[self.name] = self.summon_line
                self.servants.append(p['name'])
                self.claim_status.append(p['claim'])
                
            if not False in self.claim_status:
               self.popupmsg()
                
        with open("config.txt", "w") as jsonFile:  
            
            jsonFile.seek(0)                
            json.dump(data, jsonFile, indent = 4)  
            
    def config_reset(self):
        #Reads JSON and changes all claims to False
        with open("config.txt", "r") as jsonFile:       

            data = json.load(jsonFile)      
            
            for p in data['Servant']:
                p['claim'] = False
             
        #updates JSON file
        with open("config.txt", "w") as jsonFile:  
            
            jsonFile.seek(0)                
            json.dump(data, jsonFile, indent = 4)  
                       
    def popupmsg(self):
        popup = Tk()
        popup.wm_title("Warning")
        popup.geometry('300x100')
        popup.resizable(False, False)

        label = Label(popup, text = "All Servants have been claimed. Please reset the configuration or edit the local config file.", wraplength = 280)
        label.pack(side = "top", fill = "x", pady = 10)
        
        B1 = Button(popup, text = "Okay", command = popup.destroy)
        B1.pack()
        
        popup.mainloop()
        
    