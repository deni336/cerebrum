import tkinter as tk
from tkinter import ttk
import GUI as G

class CameraViewer(G.GUI):
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Visual", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")