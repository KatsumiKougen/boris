import tkinter as tk
from random import choice

def Start(w):
    def ChangeColourScheme(type_):
        match type_:
            case 0:
                ManualText["fg"], ManualText["bg"] = "#000", "#fff"
            case 1:
                ManualText["fg"], ManualText["bg"] = "#fff", "#000"
            case 2:
                Hex = "0123456789abcdef"
                ManualText["fg"], ManualText["bg"] = f"#{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}", f"#{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}{choice(Hex)}"
    
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("755x630")
    p.title("User Manual")
    p.resizable(False, False)
    
    UpperText = tk.Label(
        master = p,
        font = ("FOT-Rodin Pro", 14),
        text = "User manual",
        pady = 5
    )
    UpperText.grid(row=0, column=0, sticky=tk.W)
    
    LowerText = tk.Label(
        master = p,
        font = ("FOT-Rodin Pro", 10),
        text =
        	"    \"Gee, it sure is boring around here!\"\n"
        	"    \"My boy, this user manual is what all true ASCII artists strive for!\"",
    	justify = tk.LEFT,
        pady = 2
    )
    LowerText.grid(row=1, column=0, sticky=tk.W)
    
    ManualText = tk.Text(
        master = p,
        font = ("DejaVu Sans Mono", 11, "bold"),
        width = 80,
        height = 25,
        wrap = tk.CHAR,
        cursor = "left_ptr"
    )
    ManualText.grid(row=2, column=0)
    ManualText.insert("1.0", open("manual.txt", "r").read())
    ManualText["state"] = tk.DISABLED
    
    ColourSchemesFrame = tk.Frame(master=p, pady=10)
    ColourSchemesFrame.grid(row=3, column=0)
    ColourSchemeType = tk.IntVar()
    ColourSchemeRdb = [
        tk.Radiobutton(
            master = ColourSchemesFrame,
            font = ("FOT-Rodin Pro", 11),
            text = "Black on white",
            variable = ColourSchemeType,
            value = 0,
            command = lambda: ChangeColourScheme(0)
        ),
        tk.Radiobutton(
            master = ColourSchemesFrame,
            font = ("FOT-Rodin Pro", 11),
            text = "White on black",
            variable = ColourSchemeType,
            value = 1,
            command = lambda: ChangeColourScheme(1)
        ),
        tk.Radiobutton(
            master = ColourSchemesFrame,
            font = ("FOT-Rodin Pro", 11),
            text = "Whatever on LSD",
            variable = ColourSchemeType,
            value = 2,
            command = lambda: ChangeColourScheme(2)
        )
    ]
    for idx, i in enumerate(ColourSchemeRdb):
        i.grid(row=0, column=idx)
    ColourSchemeRdb[0].select()
    
    CloseButton = tk.Button(
        master = p,
        font = ("FOT-Rodin Pro", 12),
        text = "Close",
        command = p.destroy
    )
    CloseButton.grid(row=4, column=0)
