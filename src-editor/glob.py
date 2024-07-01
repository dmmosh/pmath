import sys 
import os
import tkinter as tk

r = tk.Tk() # main root window
r.title("pmath-editor")
r.grid_rowconfigure(0,minsize=400)
r.grid_columnconfigure(0,minsize=400)

text = {"edit": tk.Text(r),
        "interpret": tk.Text(r)}

text["edit"].grid(row=0,column=0)



