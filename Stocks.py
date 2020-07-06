from tkinter import *
import tkinter as tk
import os
from tkinter.filedialog import asksaveasfilename, askopenfilename
#Image Libraries
import cv2
import PIL.Image, PIL.ImageTk
import time
#Finance Libraries
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date


class FullScreenApp(object):
    #Main Function
    def __init__(self, master, **kwargs):
        self.master=master
        #Positioning and Fullscreen
        pad=3
        #Default 200x200
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<F11>',self.toggle_geom)
        #Title
        root.title("Stock Trade")
        #Menu
        menu = Menu(root)
        #Menu Buttons
        home_item = Menu(menu, tearoff=0)
        file_item = Menu(menu, tearoff=0)
        edit_item = Menu(menu, tearoff=0)
        help_item = Menu(menu, tearoff=0)
        #File Buttons
        file_item.add_command(label='Open', command=self.open_file)
        file_item.add_separator()
        file_item.add_command(label='Save', command=self.save_file)
        file_item.add_separator()

        #Edit Buttons
        menu.add_cascade(label='Home', menu=home_item)
        menu.add_cascade(label='File', menu=file_item)
        menu.add_cascade(label='Edit', menu=edit_item)
        menu.add_cascade(label='Run', command=self.run)
        menu.add_cascade(label='Help', menu=help_item)
        menu.add_cascade(label='Exit', command=self.exit)
        root.config(menu=menu)



    #Resize Handler
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
    #Run
    def run(self):
        print("run")
    #Open
    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")
    #Save
    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")
    #Exit
    def exit(self):
        root.quit()
        root.destroy()

#Call Window Manager
root=tk.Tk()
#Call Application
app=FullScreenApp(root)
#Call Loop
root.mainloop()
