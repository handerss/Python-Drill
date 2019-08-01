# Author: Anders Johnson
# 
# Tech Academy Pg 121 Drill
#
# Python Ver: 3.7.3
#

from tkinter import *
import tkinter as tk

# Import other module.. think of it like CSS and HTML
import GUI121_A




def load_gui(self):
    
    self.btn_add = tk.Button(self.master,width=30,height=4,text='Browse...')
    self.btn_add.grid(row=1,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(100,00),sticky=N+W)
    self.btn_2add = tk.Button(self.master,width=30,height=4,text='Browse...')
    self.btn_2add.grid(row=2,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(10,00),sticky=N+W)
    self.btn_ck = tk.Button(self.master,width=30,height=6,text='Check for files...')
    self.btn_ck.grid(row=5,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(20,00),sticky=N+W)
    self.btn_cls = tk.Button(self.master,width=30,height=6,text='Close Program')
    self.btn_cls.grid(row=5,column=7,rowspan=1,columnspan=1, padx=(600,0),pady=(20,00),sticky=N+W)                
    self.txt_add = tk.Entry(self.master,text='')
    self.txt_add.grid(row=1,column=2,rowspan=4,columnspan=10,padx=(40,0),ipadx=330,pady=(100,0),ipady=20,sticky=N+W)
    self.txt_add2 = tk.Entry(self.master,text='')
    self.txt_add2.grid(row=2,column=2,rowspan=4,columnspan=10,padx=(40,0),ipadx=330,pady=(10,0),ipady=20,sticky=N+W)
                    
    #self.lstList1 = Listbox(self.master)
    #self.lstList1.grid(row=1,column=1,rowspan=1,columnspan=12,padx=(30,00),pady=(100,00),sticky=N+E+S+W)



if __name__ == "__main__":
    pass
