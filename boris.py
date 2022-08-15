#!/usr/bin/env python3
#    ▛▀▖▞▀▌▛▀▖▀▛▘▞▀▘    | written in Python 3 | by Katsumi Kougen
#    ▛▀▖▌ ▌▙▞  ▌ ▝▚     | github.com/KatsumiKougen
#    ▙▄▘▙▄▘▌▝▖▄▙▖▄▄▘    | twitter.com/realKatsumi_vn
# text mode art program |
#-----------------------+--------------------------------------------------
# this program is distributed under Bisqwit's Licence:
#    no warranty. you are free to modify this source and to
#    distribute the modified sources, as long as you keep the
#    existing copyright messages intact and as long as you
#    remember to add your own copyright markings.
#    you are not allowed to distribute the program or modified versions
#    of the program without including the source code (or a reference to
#    the publicly available source) and this notice with it.

import sys, re
import bpreview as bp, bpalette as bpa, bchangebg as bg, bchartbl as bt, bcredits as bc, bfiledialog as bf, bfilehndl as bfh, bmanual as bm, bicon

DefaultPalette = "101117 b81c11 28bd37 c9a11e 374fa6 9c48ab 54aac7 818791 373b4a f54640 4ce060 f7d454 3156eb b56fed 5cd3e0 d1d3e0".split()

print(
    "\n"
    "    ▛▀▖▞▀▌▛▀▖▀▛▘▞▀▘    | written in Python 3 | by Katsumi Kougen\n"
    "    ▛▀▖▌ ▌▙▞  ▌ ▝▚     | github.com/KatsumiKougen\n"
    "    ▙▄▘▙▄▘▌▝▖▄▙▖▄▄▘    | twitter.com/realKatsumi_vn\n"
    " text mode art program |\n"
)

try:
    import tkinter as tk, clipboard as cb
    from tkinter import messagebox as mb
except ImportError:
    print("ERROR: tkinter and Pillow library not found. enter this command \"pip install tkinter pillow\".")
else:
    if len(sys.argv) > 1 and sys.argv[1] == "--ida": # Easter egg
        print(
            "▙▗▌▄▖ ▖▄  ▘ ▖▄ ▄▖    ▀▛▘▗▄▌▄▖\n"
            "▌▘▌▗▟ ▛ ▘▀▌ ▛ ▌▗▟     ▌ ▌ ▌▗▟\n"
            "▌ ▌▚▟▖▌  ▄▙▖▌ ▌▚▟▖   ▄▙▖▚▄▌▚▟▖\n"
            "gen 83 - Octoling combat engineer (whereabouts unknown)\n"
            "CLASSIFIED\n"
            "- age 6: enrolled in the elementary training program at Slimeskin Garrison.\n"
            "- age 9: skipped multiple grades. took only advanced courses. graduated.\n"
            "- age 10: member of Flooder design team (fully automated cleaning weapon).\n"
            "- age 13: joined Slimeskin Garrison. specialized in improving Great Octoweapons.\n"
            "- age 16: assigned to DJ Octavio's wasabi supply unit. earned multiple commendations.\n"
            "- same year: went AWOL after coming within audible range of the Calamari Inkantation sung by the New Squidbeak Splatoon. "
            "according to witness interviews, she said \"This changes everything,\" before vanishing."
        )
    
    class FormatEngine:
        
        DefaultColour = [0, 15]
        
        def Parse(self, s):
            self.Tags = [[string, tag] for string, tag in zip(
                re.split(r"\[[\da-f]{2}\]", s)[1:],
                re.findall(r"\[[\da-f]{2}\]", s)
            )]
            self.IsolatedTag = re.split(r"\[[\da-f]{2}\]", s)[0]
            if self.IsolatedTag != "":
                self.Tags.insert(0, [self.IsolatedTag, f"[{'0123456789abcdef'[self.DefaultColour[0]]}{'0123456789abcdef'[self.DefaultColour[1]]}]"])
    
    class GUICore:
        
        GlobalFont = ("FOT-Rodin Pro", "FOT-RodinNTLG Pro", "jgs5", "DejaVu Sans Mono")
        UndoStack = 20
        
        def __init__(self, WindowSize):
            #WindowSize = [width, height]
            self.win = tk.Tk()
            self.win.geometry(f"{WindowSize[0]}x{WindowSize[1]}")
            self.win.resizable(False, False)
            self.win.title("Boris by Katsumi")
            
            self.Engine = FormatEngine()
        
        def ExitConfirm(self, event=None):
            ExitWindow = tk.Toplevel(master=self.win, padx=10, pady=5)
            ExitWindow.geometry("320x80")
            ExitWindow.title("Exiting Boris")
            ExitWindow.resizable(False, False)
            
            Message = tk.Label(
                master = ExitWindow,
                font = (self.GlobalFont[0], 12),
                text = "Are you sure you want to exit Boris?",
                pady = 5
            )
            Message.grid(row=0, column=0, columnspan=2)
            YesButton = tk.Button(
                master = ExitWindow,
                font = (self.GlobalFont[1], 12),
                text = "Yes",
                command = self.win.destroy
            )
            YesButton.grid(row=1, column=0, sticky=tk.E)
            NoButton = tk.Button(
                master = ExitWindow,
                font = (self.GlobalFont[1], 12),
                text = "No",
                command = ExitWindow.destroy
            )
            NoButton.grid(row=1, column=1, sticky=tk.W)
        
        def SelectAll(self, event=None):
            self.InputBox.tag_add("sel", "1.0", tk.END)
            return "break"
        
        def ClipboardAction(self, action, event=None):
            match action:
                case "cut" | "CUT" | "Cut":
                    cb.copy(self.InputBox.selection_get())
                    self.InputBox.delete(tk.SEL_FIRST, tk.SEL_LAST)
                case "copy" | "COPY" | "Copy":
                    cb.copy(self.InputBox.selection_get())
                case "paste" | "PASTE" | "Paste":
                    CursorPosition = self.InputBox.index(tk.INSERT)
                    self.InputBox.insert(CursorPosition, cb.paste())
        
        def UpdateCursorPos(self, method):
            cursor = method.split(".")
            self.CursorPos["text"] = f"Ln {cursor[0]}, Col {int(cursor[1])+1}"
        
        def GrabText(self, event=None):
            self.InputString = self.InputBox.get("1.0", tk.END)[:-1]
        
        def OpenPreview(self, event=None):
            if self.Engine.Tags == None or len(self.Engine.Tags) == 0:
                mb.showerror("An error has occured", "There's no text to output. Type something!")
            else:
                bp.Start(self.win, self.Engine.Tags, DefaultPalette, self.Engine.DefaultColour[0], self.Engine.DefaultColour[1])
        
        def OpenChangeBg(self, event=None):
            self.Engine.DefaultColour = bg.Start(self.win, DefaultPalette, self.Engine.DefaultColour[0], self.Engine.DefaultColour[1])
        
        def OpenPalette(self, event=None):
            bpa.Start(self.win, DefaultPalette)
        
        def OpenCharTable(self, event=None):
            bt.Start(self.win)
        
        def OpenUserManual(self, event=None):
            bm.Start(self.win)
        
        def OpenCredits(self):
            bc.Start(self.win)
        
        def SaveFile(self, event=None):
            try:
                file = bf.Start(self.win, "save")
                if file[1] in "ugf ugfr json".split():
                    bfh.FileHandler("save", file[1], self.Engine.Tags).Write(file[0])
                else:
                    bfh.FileHandler("save", file[1], self.InputString).Write(file[0])
            except AttributeError:
                pass
        
        def OpenFile(self, event=None):
            try:
                file = bf.Start(self.win, "load")
                Buffer = bfh.FileHandler("load", file[1], file[0]).Read()
                self.InputBox.delete("1.0", tk.END)
                if file[1] in "ugf ugfr json".split():
                    self.InputBox.insert("1.0", "".join(["".join([i[1], i[0]]) for i in Buffer]))
                    self.InputString = "".join(["".join([i[1], i[0]]) for i in Buffer])
                else:
                    self.InputBox.insert("1.0", Buffer)
                    self.InputString = Buffer
                self.Engine.Parse(self.InputString)
            except AttributeError:
                pass
        
        def PlaceMenu(self):
            # SM = Sub menu
            self.Menu = tk.Menu(master=self.win)
            self.win["menu"] = self.Menu
            
            self.SMFile = tk.Menu(master=self.Menu, tearoff=0)
            self.Menu.add_cascade(
                label = "File",
                menu = self.SMFile,
                underline = 0
            )
            for i, cmd, u, ac in zip(
                "Open\0Save\0\x01\0Exit".split("\0"),
                [self.OpenFile, self.SaveFile, None, self.ExitConfirm],
                [0, 0, -1, 1],
                ["Ctrl+O", "Ctrl+S", None, "Alt+F4"]
            ):
                if i != "\x01":
                    if u != -1:
                        if ac != None:
                            self.SMFile.add_command(label=i, command=cmd, underline=u, accelerator=ac)
                        else:
                            self.SMFile.add_command(label=i, command=cmd, underline=u)
                    else:
                        if ac != None:
                            self.SMFile.add_command(label=i, command=cmd, accelerator=ac)
                        else:
                            self.SMFile.add_command(label=i, command=cmd)
                else:
                    self.SMFile.add_separator()
            
            self.SMEdit = tk.Menu(master=self.Menu, tearoff=0)
            self.Menu.add_cascade(
                label = "Edit",
                menu = self.SMEdit,
                underline = 0
            )
            for i, cmd, u, ac in zip(
                "Undo\0Redo\0\x01\0Cut\0Copy\0Paste\0Select All".split("\0"),
                [self.InputBox.edit_undo, self.InputBox.edit_redo, None, lambda: self.ClipboardAction("cut"), lambda: self.ClipboardAction("copy"), lambda: self.ClipboardAction("paste"), self.SelectAll],
                [0, 0, -1, 2, 0, 0, 7],
                ["Ctrl+Z", "Ctrl+Shift+Z", None, "Ctrl+X", "Ctrl+C", "Ctrl+V", "Ctrl+A"]
            ):
                if i != "\x01":
                    if u != -1:
                        if ac != None:
                            self.SMEdit.add_command(label=i, command=cmd, underline=u, accelerator=ac)
                        else:
                            self.SMEdit.add_command(label=i, command=cmd, underline=u)
                    else:
                        if ac != None:
                            self.SMEdit.add_command(label=i, command=cmd, accelerator=ac)
                        else:
                            self.SMEdit.add_command(label=i, command=cmd)
                else:
                    self.SMEdit.add_separator()
            
            self.SMTools = tk.Menu(master=self.Menu, tearoff=0)
            self.Menu.add_cascade(
                label = "Tools",
                menu = self.SMTools,
                underline = 0
            )
            for i, cmd, u, ac in zip(
                "Preview\0\x01\0View Colour Palette\0Change Foreground and Background Colour\0\x01\0Character Table".split("\0"),
                [self.OpenPreview, None, self.OpenPalette, self.OpenChangeBg, None, self.OpenCharTable],
                [0, -1, 2, 0, -1, 10],
                ["Ctrl+P", None, "Ctrl+G", "Ctrl+Q", None, "F1"]
            ):
                if i != "\x01":
                    if u != -1:
                        if ac != None:
                            self.SMTools.add_command(label=i, command=cmd, underline=u, accelerator=ac)
                        else:
                            self.SMTools.add_command(label=i, command=cmd, underline=u)
                    else:
                        if ac != None:
                            self.SMTools.add_command(label=i, command=cmd, accelerator=ac)
                        else:
                            self.SMTools.add_command(label=i, command=cmd)
                else:
                    self.SMTools.add_separator()
            
            self.SMHelp = tk.Menu(master=self.Menu, tearoff=0)
            self.Menu.add_cascade(
                label = "Help",
                menu = self.SMHelp,
                underline = 0
            )
            for i, cmd, u, ac in zip(
                "User Manual\0About Boris".split("\0"),
                [self.OpenUserManual, self.OpenCredits],
                [5, 0],
                ["F2", None]
            ):
                if i != "\x01":
                    if u != -1:
                        if ac != None:
                            self.SMHelp.add_command(label=i, command=cmd, underline=u, accelerator=ac)
                        else:
                            self.SMHelp.add_command(label=i, command=cmd, underline=u)
                    else:
                        if ac != None:
                            self.SMHelp.add_command(label=i, command=cmd, accelerator=ac)
                        else:
                            self.SMHelp.add_command(label=i, command=cmd)
                else:
                    self.SMHelp.add_separator()
        
        def PlaceFrames(self):
            def PlaceLeftFrame():
                self.LeftFrame = tk.Frame(
                    master = self.win,
                    padx = 10,
                    pady = 10
                )
                self.LeftFrame.grid(row=0, column=0)
                self.InputBox = tk.Text(
                    master = self.LeftFrame,
                    height = 25,
                    width = 60,
                    selectbackground = "#3378e8",
                    selectforeground = "#fff",
                    font = (self.GlobalFont[2], 13),
                    wrap = tk.CHAR,
                    undo = True,
                    maxundo = self.UndoStack
                )
                self.InputBox.grid(row=0, column=0)
            
            def PlaceRightFrame():
                self.RightFrame = tk.Frame(master=self.win)
                self.RightFrame.grid(row=0, column=1, sticky=tk.N)
                self.PrgTitleFrame = tk.Frame(master=self.RightFrame)
                self.PrgTitleFrame.grid(row=0, column=0)
                self.PrgTitle = [
                    tk.Label(
                        master = self.PrgTitleFrame,
                        font = (self.GlobalFont[3], 10, "bold"),
                        text =
                            "┌──┐\n"
                            "│  └┐   it's just...\n"
                            "│  ┌┘         ∙\n"
                            "├──┤ ┌──┐┌──┐─┐ ┌──┐\n"
                            "│  └┐│  ││    │ └──┐\n"
                            "│  ┌┘│  ││    │    │\n"
                            "└──┘ └──┘┴  ──┴─└──┘",
                        justify = tk.LEFT
                    ),
                    tk.Label(
                        master = self.PrgTitleFrame,
                        font = (self.GlobalFont[0], 11),
                        text = "Version 0.1\nby Katsumi"
                    )
                ]
                for idx, i in enumerate(self.PrgTitle):
                    i.grid(row=idx, column=0)
                self.GuideFrame = tk.Frame(
                    master = self.RightFrame,
                    pady = 10
                )
                self.GuideFrame.grid(row=1, column=0)
                self.GuideText = [
                    [
                        tk.Label(
                            master = self.GuideFrame,
                            font = (self.GlobalFont[0], 22),
                            text = "⬅️"
                        ),
                        tk.Label(
                            master = self.GuideFrame,
                            font = (self.GlobalFont[0], 15),
                            text = "Type\nsomething\nhere"
                        )
                    ],
                    [
                        None,
                        tk.Label(
                            master = self.GuideFrame,
                            font = (self.GlobalFont[0], 15),
                            text = "View your\nartwork\nhere"
                        )
                    ],
                    [
                        None,
                        tk.Label(
                            master = self.GuideFrame,
                            font = (self.GlobalFont[0], 22),
                            text = "⬇️"
                        )
                    ]
                ]
                for idx0, y in enumerate(self.GuideText):
                    for idx1, x in enumerate(y):
                        if x != None:
                            x.grid(row=idx0, column=idx1)
                self.PreviewButton = tk.Button(
                    master = self.RightFrame,
                    font = (self.GlobalFont[1], 12),
                    text = "Preview",
                    command = self.OpenPreview
                )
                self.PreviewButton.grid(row=2, column=0)
                self.PaletteButton = tk.Button(
                    master = self.RightFrame,
                    font = (self.GlobalFont[1], 12),
                    text = "Palette",
                    command = self.OpenPalette
                )
                self.PaletteButton.grid(row=3, column=0)
                self.SaveButton = tk.Button(
                    master = self.RightFrame,
                    font = (self.GlobalFont[1], 12),
                    text = "Save",
                    command = self.SaveFile
                )
                self.SaveButton.grid(row=4, column=0)
                self.LoadButton = tk.Button(
                    master = self.RightFrame,
                    font = (self.GlobalFont[1], 12),
                    text = "Load",
                    command = self.OpenFile
                )
                self.LoadButton.grid(row=5, column=0)
            
            def PlaceBottomFrame():
                self.BottomFrame = tk.Frame(
                    master = self.win,
                    padx = 14
                )
                self.BottomFrame.grid(row=1, column=0, columnspan=2, sticky=tk.W)
                self.CursorPos = tk.Label(
                    master = self.BottomFrame,
                    font = (self.GlobalFont[0], 9),
                    text = "Ln 1, Col 1"
                )
                self.CursorPos.grid(row=0, column=0)
            
            PlaceLeftFrame()
            PlaceRightFrame()
            PlaceBottomFrame()
        
        def AddEvents(self):
            # File
            self.win.protocol("WM_DELETE_WINDOW", self.ExitConfirm)
            self.win.bind("<Control-O>", self.OpenFile)
            self.win.bind("<Control-o>", self.OpenFile)
            self.win.bind("<Control-S>", self.SaveFile)
            self.win.bind("<Control-s>", self.SaveFile)
            # Edit
            self.InputBox.bind("<Control-A>", self.SelectAll)
            self.InputBox.bind("<Control-a>", self.SelectAll)
            # Tools
            self.win.bind("<Control-P>", self.OpenPreview)
            self.win.bind("<Control-p>", self.OpenPreview)
            self.win.bind("<Control-G>", self.OpenPalette)
            self.win.bind("<Control-g>", self.OpenPalette)
            self.win.bind("<Control-Q>", self.OpenChangeBg)
            self.win.bind("<Control-q>", self.OpenChangeBg)
            self.win.bind("<F1>", self.OpenCharTable)
            # Other
            self.win.bind("<F2>", self.OpenUserManual)
            self.InputBox.bind("<KeyRelease>", lambda _: self.UpdateCursorPos(self.InputBox.index("insert")))
            self.InputBox.bind("<KeyRelease>", self.GrabText, add="+")
            self.InputBox.bind("<KeyRelease>", lambda _: self.Engine.Parse(self.InputString), add="+")
        
        def Start(self):
            self.Engine.Tags = None
            self.PlaceFrames()
            self.PlaceMenu()
            self.AddEvents()
            bicon.initStdIcon(self.win)
            self.win.mainloop()
    
    main = GUICore([750, 500])
    main.Start()
