# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:54:40 2019

@author: Justin Corcuera
"""
from tkinter import * 
from ConfigUtility import ConfigUtility

class OptionMenu():
    
    def __init__(self, menu, root):
        option_menu = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "Options", menu = option_menu)
        
        option_menu.add_command(label = "View Claimed", command = self.view)
        option_menu.add_separator()
        option_menu.add_command(label = "Exit",command = root.destroy)
        
    def view(self):         
        window = Tk()
        window.geometry("400x320")
        
        fr=Frame(window)
        fr.pack()
        
        #create scrollbar
        sbr = Scrollbar(fr)
        sbr.pack(side = RIGHT,fill= "y")
        
        #create listbox
        lbx = Listbox(fr, font = ("Verdana",16))
        lbx.pack(side = LEFT,fill = "both", expand=1)
        
        #Fill listbox will all claimed Servants
        util = ConfigUtility()
        claim = util.claimed()
        servant = util.get_all()
        
        #Iterates through all Servants and adds only those who are claimed
        for i in servant:
            if claim[i] == True:               
                lbx.insert(END, i)
        
        #link scrollbar and listbox
        sbr.config(command=lbx.yview)
        lbx.config(yscrollcommand=sbr.set)
        
        #Creatin Label to house Buttons
        hbox = Label(window)
        hbox.pack(side = BOTTOM, pady = 2)
        
        #Creating Buttons
        button = Button(hbox, text = "Unclaim All", bg = "#DAD9D9", padx = 10, pady = 2, command = lambda: self.unclaim_popupmsg(lbx))
        button.grid(row=0, column=1, padx=10, pady=10)
        
        button2 = Button(hbox, text = "Close", bg = "#DAD9D9", padx = 10, pady = 2, command = lambda: window.destroy())
        button2.grid(row=0, column=2, padx=10, pady=10)
        
        window.mainloop()
        
        #calls config utility to unclaim all and update the listbox
    def unclaim(self, popup, lbx):
        #resets all claim values
        util = ConfigUtility()
        util.config_reset()
        
        #Clears the list box
        lbx.delete(0, END)
        
        popup.destroy()
    
    def unclaim_popupmsg(self, lbx):
        popup = Tk()
        popup.wm_title("Warning")
        popup.geometry('300x200')
        popup.resizable(False, False)

        label = Label(popup, text = "Are you sure you want to unclaim all Servants?")
        label.pack(side = "top", fill = "x", pady = 10)
        
        #Creatin Label to house Buttons
        hbox = Label(popup)
        hbox.pack(side = BOTTOM, pady = 2)
        
        #Creating Button
        button = Button(hbox, text = "Unclaim All", bg = "#DAD9D9", padx = 10, pady = 2, command = lambda: self.unclaim(popup, lbx))
        button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        button2 = Button(hbox, text = "Close", bg = "#DAD9D9", padx = 10, pady = 2, command = lambda: popup.destroy())
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)  
        
        popup.mainloop()
    