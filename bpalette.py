import tkinter as tk
from PIL import Image, ImageTk

def Start(w, palette):
    def SmallImage(filename, scalefactor=1.0):
        image = Image.open(filename)
        out = ImageTk.PhotoImage(image.resize(tuple(map(int, [float(scalefactor) * image.size[0], float(scalefactor) * image.size[1]])), Image.ANTIALIAS))
        return out
    
    Palette = palette
    ColourName = "Black\n\0Crimson\n\0Dark\ngreen\0Dark\nyellow\0Cobalt\nblue\0Violet\n\0Dark\ncyan\0Gray\n\0Dark\ngray\0Red\n\0Green\n\0Yellow\n\0Blue\n\0Magenta\n\0Cyan\n\0White\n".split("\0")
    Sample = SmallImage("img/MeggySpletzer.png", .055)
    
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("800x320")
    p.title("Colour Palette")
    p.resizable(False, False)
    
    UpperText = tk.Label(
        master = p,
        font = ("FOT-Rodin Pro", 14),
        text = "Standard colour palette",
        pady = 5
    )
    UpperText.grid(row=0, column=0, sticky=tk.W)
    
    PaletteTable = tk.Frame(master=p, relief=tk.SUNKEN, bd=2)
    PaletteTable.grid(row=1, column=0, sticky=tk.N+tk.W)
    
    ColourCell = [
        tk.Frame(master=PaletteTable, padx=5, pady=10)
        for i in range(16)
    ]
    ColourRepr = [
        [
            tk.Label(
                master = ColourCell[i],
                image = Sample,
                bg = f"#{Palette[i]}",
                relief = tk.RAISED,
                bd = 2,
                padx = 3,
                pady = 10
            ),
            tk.Label(
                master = ColourCell[i],
                font = ("FOT-RodinNTLG Pro", 9),
                text = ColourName[i]
            ),
            tk.Label(
                master = ColourCell[i],
                font = ("DejaVu Sans Mono", 12),
                text = "0123456789abcdef"[i]
            )
        ]
        for i in range(16)
    ]
    for idx0, i in enumerate([ColourCell[:8], ColourCell[8:]]):
        for idx1, cell in enumerate(i):
            cell.grid(row=idx0, column=idx1)
    for idx0, i in enumerate([ColourRepr[:8], ColourRepr[8:]]):
        for idx1, group in enumerate(i):
            group[0].grid(row=0, column=0)
            group[0].image = Sample
            group[1].grid(row=1, column=0)
            group[2].grid(row=2, column=0)
    
    CloseButton = tk.Button(
        master = p,
        font = ("FOT-Rodin Pro", 12),
        text = "Close",
        command = p.destroy
    )
    CloseButton.grid(row=2, column=0)
