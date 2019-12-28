## -*- coding: utf-8 -*-
#"""
#Created on Fri Dec 27 15:01:35 2019
#
#@author: Justin Corcuera
#"""
import json
import random 

class ConfigUtility():
    
    def __init__(self):
        self.name_to_class = {}
        self.name_to_claim = {}
        self.name_to_appear = {}
        self.name_to_pic = {}
        self.name_to_line = {}
        self.servants = []
        
        #Opens JSON config and assigns to variables. TODO:Change open and the file itself to .json
        with open('config.txt') as json_file:
            data = json.load(json_file)
            for p in data['Servant']:
                self.name = p['name']
                self.f_class = p['f_class']
                self.claim = p['claim']
                self.appear = p['appear']
                self.pic_url = p['pic_url']
                self.summon_line = p['line']
                self.name_to_class[self.name] = self.f_class
                self.name_to_claim[self.name] = self.claim
                self.name_to_appear[self.name] = self.appear
                self.name_to_pic[self.name] = self.pic_url
                self.name_to_line[self.name] = self.summon_line
                self.servants.append(p['name'])

    #Gets random Servant Name                
    def get_random(self):
        return self.servants[random.randint(0, 1)] #TODO: servants.len for the random int length

    #Passes dict with names mapped to class
    def class_dict(self):
        return self.name_to_class
    
    #Passes dict with names mapped to claim status    
    def claimed(self):
        return self.name_to_claim

    #Passes dict with names mapped to appear status 
    def appearable(self):
        return self.name_to_appear

    #Passes dict with names mapped to pic url
    def pic_dict(self):
        return self.name_to_pic
    
    def line_dict(self):
        return self.name_to_line
    
    def update_config(self, servant):
        print("TODO: Update Config")
        #TODO: Update the config with new claim and appearnce values
        
    