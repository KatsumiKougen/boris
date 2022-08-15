import tkinter as tk, chartable as ctb, clipboard as cb
from tkinter import ttk

def Start(w):
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("615x300")
    p.title("Character Table")
    p.resizable(False, False)
    
    CharGroupsFrame = tk.Frame(master=p, pady=7)
    CharGroupsFrame.grid(row=0, column=0, sticky=tk.W)
    CharGroupsTabber = ttk.Notebook(master=CharGroupsFrame)
    CharGroupsTabber.grid(row=0, column=0)
    
    CharGroupsTable0 = tk.Frame(master=CharGroupsFrame, bd=2, relief=tk.SUNKEN)
    CharGroupsTable1 = tk.Frame(master=CharGroupsFrame, bd=2, relief=tk.SUNKEN)
    CharGroupsTable2 = tk.Frame(master=CharGroupsFrame, bd=2, relief=tk.SUNKEN)
    CharSet = [
        ctb.CharTable(CharGroupsTable0, "BasicLatin"),
        ctb.CharTable(CharGroupsTable1, "AdditionalChar"),
        ctb.CharTable(CharGroupsTable2, "GlyphSemigraph"),
    ]
    
    CharGroupsTabber.add(CharGroupsTable0, text="Basic Latin")
    CharGroupsTabber.add(CharGroupsTable1, text="Additional Characters")
    CharGroupsTabber.add(CharGroupsTable2, text="Glyphs and Semigraphics")
    
    for i in CharSet:
        for RowIdx, r in enumerate(i):
            for ColIdx, c in enumerate(r):
                c.grid(row=RowIdx, column=ColIdx)
    
    CloseButton = tk.Button(
        master = p,
        font = ("FOT-Rodin Pro", 12),
        text = "Close",
        command = p.destroy
    )
    CloseButton.grid(row=1, column=0)
