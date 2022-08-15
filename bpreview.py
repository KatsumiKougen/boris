import tkinter as tk

Hex = "0123456789abcdef"

def Start(w, tags, palette, fg=0, bg=15):
    def InitColour():
        for bg in Hex:
            for fg in Hex:
                PreviewWidget.tag_config(
                    f"{fg}{bg}",
                    foreground = f"#{palette[Hex.index(fg)]}",
                    background = f"#{palette[Hex.index(bg)]}",
                )
    
    p = tk.Toplevel(master=w, padx=15, pady=15)
    p.geometry("575x520")
    p.title("Preview")
    p.resizable(False, False)
    
    PreviewWidget = tk.Text(
        master = p,
        fg = f"#{palette[fg]}",
        bg = f"#{palette[bg]}",
        font = ("jgs5", 13),
        width = 60,
        height = 25,
        cursor = "left_ptr"
    )
    PreviewWidget.grid(row=0, column=0)
    InitColour()
    
    CloseButton = tk.Button(
        master = p,
        font = ("FOT-Rodin Pro", 12),
        text = "Close",
        command = p.destroy
    )
    CloseButton.grid(row=1, column=0)
    
    for tag in tags:
        PreviewWidget.insert("current", tag[0])
        if len(tag[1]) == 4:
            PreviewWidget.tag_add(tag[1][1:3], f"insert-{len(tag[0])}c", "current")
        elif len(tag[1]) == 3:
            PreviewWidget.tag_add(f"{tag[1][1]}f", f"insert-{len(tag[0])}c", "current")
    PreviewWidget["state"] = tk.DISABLED
