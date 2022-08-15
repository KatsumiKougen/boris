import tkinter as tk

def Start(w, palette, fg=0, bg=15):
    def UpdatePreview(event=None):
        PreviewText["fg"] = f"#{palette[Colours[0].get()]}"
        PreviewText["bg"] = f"#{palette[Colours[1].get()]}"
    
    def Unlock():
        ChangeLock = True
        p.destroy()
    
    ChangeLock = False
    
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("445x290")
    p.title("Change Foreground and Background Colour")
    p.resizable(False, False)
    
    Colours = [tk.IntVar(), tk.IntVar()]
    
    UpperText = tk.Label(
        master = p,
        font = ("FOT-Rodin Pro", 14),
        text = "Change foreground and background colour"
    )
    UpperText.grid(row=0, column=0)
    
    MiddleFrame = tk.Frame(master=p, pady=15)
    MiddleFrame.grid(row=1, column=0)
    PreviewText = tk.Label(
        master = MiddleFrame,
        font = ("jgs5", 32),
        text = "SHUW\nATCH",
        fg = f"#{palette[fg]}",
        bg = f"#{palette[bg]}",
        relief = tk.GROOVE,
        bd = 3,
        padx = 12,
        pady = 12
    )
    PreviewText.grid(row=0, column=0)
    ScaleFrame = tk.Frame(master=MiddleFrame, padx=10)
    ScaleFrame.grid(row=0, column=1)
    FgScale = tk.Scale(
        master = ScaleFrame,
        font = ("FOT-Rodin Pro", 8),
        label = "Foreground",
        length = 180,
        width = 30,
        orient = tk.HORIZONTAL,
        from_ = 0.0,
        to = 15.0,
        digits = 1,
        resolution = -1,
        repeatdelay = 5000,
        tickinterval = 4.0,
        variable = Colours[0],
        command = UpdatePreview
    )
    BgScale = tk.Scale(
        master = ScaleFrame,
        font = ("FOT-Rodin Pro", 8),
        label = "Background",
        length = 180,
        width = 30,
        orient = tk.HORIZONTAL,
        from_ = 0.0,
        to = 15.0,
        digits = 1,
        resolution = -1,
        repeatdelay = 5000,
        tickinterval = 4.0,
        variable = Colours[1],
        command = UpdatePreview
    )
    FgScale.grid(row=0, column=0)
    BgScale.grid(row=1, column=0)
    FgScale.set(fg)
    BgScale.set(bg)
    
    BottomFrame = tk.Frame(master=p)
    BottomFrame.grid(row=2, column=0)
    ApplyButton = tk.Button(
        master = BottomFrame,
        font = ("FOT-Rodin Pro", 12),
        text = "Apply",
        command = Unlock
    )
    ApplyButton.grid(row=0, column=0)
    CancelButton = tk.Button(
        master = BottomFrame,
        font = ("FOT-Rodin Pro", 12),
        text = "Cancel",
        command = p.destroy
    )
    CancelButton.grid(row=0, column=1)
    
    p.wait_window()
    
    if not ChangeLock:
        return [Colours[0].get(), Colours[1].get()]
    else:
        return [fg, bg]
