# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:10:43 2019

@author: Justin Corcuera
"""
#TODO: Delete after kyle finishes setting up the JSON

import json

data = {}
data['Servant'] = []

data['Servant'].append({
        'name': 'Jeanne Alter Santa Lily',
        'f_class': 'Lancer',
        'claim': False,
        'appear': True,
        'pic_url': 'test.png',
        'line': "I'm Jeanne! It's a bit early for Christmas but, let's do our best together! By the way, do you know how this Sled moves?"
})

data['Servant'].append({
        'name': 'Artoria',
        'f_class': 'Saber',
        'claim': False,
        'appear': True,
        'pic_url': 'test1.png',
        'line': "I ask of you. Are you my Master?"
})

#create JSON
with open('config.txt', 'w') as outfile:
    json.dump(data, outfile, indent = 4)
    
#Read JSON
#example = {}
#
#with open('congif.txt') as json_file:
#    data = json.load(json_file)
#    for p in data['Servant']:
#        name = p['name']
#        f_class = p['f_class']
#        example[name] = f_class
#        
#
#print(example['Artoria'])
        