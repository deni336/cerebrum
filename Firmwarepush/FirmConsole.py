import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Entry

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

class MyApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        mainFrame.pack_propagate(0)
        mainFrame.pack(fill="both", expand="true")
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        self.geometry("1024x600")
        self.frames = {}
        pages = (FirmwarePush, SettingsPage)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(FirmwarePush)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def quitApplication(self):
        self.destroy()

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu", menu=menu_file)
        
        menu_file.add_command(label="Firmware",
                              command=lambda: parent.showFrame(FirmwarePush))
        
        menu_file.add_command(label="Settings",
                              command=lambda: parent.showFrame(SettingsPage))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)
      

class GUI(tk.Frame):
    
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        # self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both", expand="true")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)

class FirmwarePush(GUI):
    
    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Firmware", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, frameStyles, text="Firmware")
        frame1.place(rely=0.05, relx=0.58, height=800, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, frameStyles, text="Control")
        frame2.place(rely=0.05, relx=0.02, height=400, width=600)

        sourceBtn = ttk.Button(frame2, text="Source")
        sourceBtn.pack()
        selectCamBtn = ttk.Button(frame2, text="Select Camera")
        selectCamBtn.pack()
        

class SettingsPage(GUI):

    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                        text="Settings", background="#4b4b4b",
                        foreground="blue")
        label1.pack(side="top")


root = MyApp()
app = FullScreenApp(root)
root.title("Firmware Pusher")
root.mainloop()

