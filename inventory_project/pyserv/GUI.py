import tkinter as tk

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

class GUI(tk.Frame):
    
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        # self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both", expand="true")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)