import tkinter as tk

def initStdIcon(root):
    StdIcon = tk.PhotoImage(file="img/boris_icon.png")
    root.wm_iconphoto(False, StdIcon)
