import sys 
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
from utils import *

r = tk.Tk() # main root window
r.title("pmath-editor")
r.grid_rowconfigure(0,minsize=400)
r.grid_columnconfigure(1,minsize=400)


menubar = tk.Menu(r) # MENU BAR

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=test)
filemenu.add_command(label="Open", command=test)
filemenu.add_command(label="Save", command=test)
filemenu.add_command(label="Save as...", command=test)
filemenu.add_command(label="Close", command=test)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=r.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=test)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=test)
editmenu.add_command(label="Copy", command=test)
editmenu.add_command(label="Paste", command=test)
editmenu.add_command(label="Delete", command=test)
editmenu.add_command(label="Select All", command=test)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=test)
helpmenu.add_command(label="About...", command=test)
menubar.add_cascade(label="Help", menu=helpmenu)
r.config(menu=menubar)



text = {"edit": tk.Text(r),
        "interpret": tk.Text(r)}

text["edit"].grid(row=0,column=1)



