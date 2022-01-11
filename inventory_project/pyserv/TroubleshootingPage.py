import tkinter as tk
from tkinter import ttk
import GUI as G

class TroubleshootingPage(G.GUI):
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Troubleshooting", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles)
        frame1.place(rely=0.05, relx=0.58, height=800, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Firmware Update")
        frame2.place(rely=0.05, relx=0.02, height=400, width=600)

        sourceBtn = ttk.Button(frame2, text="Source")
        sourceBtn.pack()
        selectCamBtn = ttk.Button(frame2, text="Select Camera")
        selectCamBtn.pack()