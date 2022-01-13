import tkinter as tk
from tkinter import ttk
import os
import GUI as G
import ProcessControl as PC

class TroubleshootingPage(G.GUI):
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Troubleshooting", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Search and Destroy Troubleshooter")
        frame1.place(rely=0.05, relx=0.58, height=800, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Firmware Update")
        frame2.place(rely=0.05, relx=0.02, height=400, width=600)

        sourceBtn = ttk.Button(frame2, text="Source")
        sourceBtn.pack()
        selectCamBtn = ttk.Button(frame2, text="Select Camera")
        selectCamBtn.pack()
        
        camWebPageBtn = ttk.Button(frame1, text="Camera Web Page")
        camWebPageBtn.grid()
        eventViewerBtn = ttk.Button(frame1, text="Event Viewer", command=lambda: PC.ItemViewProcesses.openEventViewer(self))
        eventViewerBtn.grid()
        viperLogsBtn = ttk.Button(frame1, text="Viper Error Logs", command=lambda: os.startfile("C:\\ViperConfigData\\Logs"))
        viperLogsBtn.grid()
        ebusPlayerbtn = ttk.Button(frame1, text="EBUS Player", command=lambda: PC.ItemViewProcesses.openEBUS(self))
        ebusPlayerbtn.grid()
        apaxUtilityBtn = ttk.Button(frame1, text="APAX Utility")
        apaxUtilityBtn.grid()
        dockPanelDeletebtn = ttk.Button(frame1, text="UI Config Folder", command=lambda: os.startfile("C:\\Users\\denis\\AppData\\Roaming\\Viper Imaging\\ViperVision"))
        dockPanelDeletebtn.grid()