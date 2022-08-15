import tkinter.filedialog

def Start(w, operation):
    StandardFileTypes = [(label, pattern) for label, pattern in zip(
        "Ultra Graphics file (encoded)\0Ultra Graphics file (raw)\0JSON file\0Text file\0Whatever extension you want".split("\0"),
        "*.ugf *.ugfr *.json *.txt *.*".split()
    )]
    
    match operation:
        case "save" | "SAVE" | "Save":
            SaveFilePath = tkinter.filedialog.asksaveasfilename(
                master = w,
                title = "Save As",
                filetypes = StandardFileTypes,
                defaultextension = ".ugf",
                initialdir = "./examples",
                initialfile = "Untitled.ugf"
            )
            SaveFileExtension = SaveFilePath.split("/")[-1].split(".")[-1]
            return SaveFilePath, SaveFileExtension
        case "load" | "LOAD" | "Load":
            OpenFilePath = tkinter.filedialog.askopenfilename(
                master = w,
                title = "Open",
                filetypes = StandardFileTypes,
                defaultextension = ".ugf",
                initialdir = "./examples",
            )
            OpenFileExtension = OpenFilePath.split("/")[-1].split(".")[-1]
            return OpenFilePath, OpenFileExtension
