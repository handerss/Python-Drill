# Author: Anders Johnson
# 
# Tech Academy Pg 121 Drill
#
# Python Ver: 3.7.3
#
from tkinter import *
import tkinter as tk

# Import other module, use correct spelling Anders!!
import GUI121_B


# Class will be inherited from Frame

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        self.master = master
        
        self.master.minsize(1110,430) #(height,width)
       
        self.master.maxsize(1110,430)
        self.master.title("Check Fles")
        self.master.configure(bg="#F0F0F0")
        

        # Load in the GUI from other module (think CSS and HTML)
        
        GUI121_B.load_gui(self)

        # **Top of the window
        
        
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
