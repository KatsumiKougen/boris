import tkinter as tk
from PIL import Image, ImageTk

def Start(w):
    def SmallImage(filename, scalefactor=1.0):
        image = Image.open(filename)
        out = ImageTk.PhotoImage(image.resize(tuple(map(int, [float(scalefactor) * image.size[0], float(scalefactor) * image.size[1]])), Image.ANTIALIAS))
        return out
    
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("565x360")
    p.title("About Boris")
    p.resizable(False, False)
    
    Sample = SmallImage("img/boris_icon.png", 0.18)
    
    PrgLogo = tk.Label(
        master = p,
        image = Sample
    )
    PrgLogo.grid(row=0, column=0)
    PrgLogo.image = Sample
    
    AdditionalInfo = tk.Frame(master=p, padx=7)
    AdditionalInfo.grid(row=0, column=1)
    
    MoreTexts = [
        tk.Label(
            master = AdditionalInfo,
            font = ("FOT-Rodin Pro", 14),
            text = "Boris — for ASCII art\nenthusiasts",
            justify = tk.LEFT
        ),
        tk.Label(
            master = AdditionalInfo,
            font = ("FOT-Rodin Pro", 10),
            text =
                "Written by your friendly neighbour Katsumi,\n"
                "a lazyass who does nothing but writing\n"
                "these programs just because... he feels\n"
                "like it. |:3",
            justify = tk.LEFT
        ),
        tk.Label(
            master = AdditionalInfo,
            font = ("FOT-Rodin Pro", 10),
            text =
                "Special thanks to:\n"
                "∙ Polyducks (for giving me inspiration\n"
                "  to write this program.)\n"
                "∙ Adel Faure (for his jgs5 font)\n"
                "∙ SMG4 / Glitch Productions (for letting\n"
                "  me use an image of their character,\n"
                "  Meggy Spletzer)",
            justify = tk.LEFT
        ),
        tk.Label(
            master = p,
            font = ("FOT-Rodin Pro", 10, "italic"),
            text =
                "This program and its source codes is available for everyone to use and modify.\n"
                "You may make any change to the sources however you want and/or distribute\n"
                "it as long as you retain the existing copyright notice and any reference to the\n"
                "publicly available source.",
            pady = 15,
            justify = tk.LEFT
        )
    ]
    for idx, i in enumerate(MoreTexts[:3]):
        i.grid(row=idx, column=0, sticky=tk.N+tk.W)
    MoreTexts[3].grid(row=1, column=0, columnspan=2)
    
    CloseButton = tk.Button(
        master = p,
        font = ("FOT-Rodin Pro", 12),
        text = "Close",
        command = p.destroy
    )
    CloseButton.grid(row=2, column=0, columnspan=2)
