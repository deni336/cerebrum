import tkinter as tk
from tkinter import ttk
from tkinter.constants import NO
import GUI as G
import ProcessControl as PC

class AdminPage(G.GUI):
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Admin", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")
        frame1 = tk.LabelFrame(self, G.frameStyles,
                               text="Historical Database Changes", background="#4b4b4b")
        frame1.place(rely=0.05, relx=0.01, height=600, width=1800)
        frame2 = tk.LabelFrame(self, G.frameStyles,
                               text="Database Control", background="#4b4b4b")
        frame2.place(rely=0.65, relx=0.75, height=100, width=200)
        button1 = ttk.Button(frame2,
                             text="Create Database", command=lambda:
                             PC.DatabaseCreationProcesses.createDatabase(self))
        button1.pack()
        button2 = ttk.Button(frame2,
                             text="Database Backup", command=lambda:
                             PC.DatabaseCreationProcesses.backupDatabase(self))
        button2.pack()
        button3 = ttk.Button(frame2,
                             text="Restore Database", command=lambda:
                             PC.DatabaseCreationProcesses.restoreFromBackup(self))
        button3.pack()
        
        tv5 = ttk.Treeview(frame1)
        columnListAccount = ["", "", "", "", "", "", "", "", "", "", ""]
        tv5['columns'] = columnListAccount
        tv5["show"] = "headings" 
        for column in columnListAccount:
            tv5.heading(column, text=column)
            tv5.column(column, width=10, stretch=NO)
        tv5.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame1)
        treeScrollY.configure(command=tv5.yview)
        tv5.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        def populate(self):
            cameraTable = PC.ItemViewProcesses.viewCameraTable(self, PC.history)
            workerTable = PC.ItemViewProcesses.viewWorkerTable(self, PC.history)
            jobTable = PC.ItemViewProcesses.viewJobTable(self, PC.history)
            computerTable = PC.ItemViewProcesses.viewComputerTable(self, PC.history)
            for row in cameraTable:
                tv5.insert("", "end", values=row)
            for row in workerTable:
                tv5.insert("", "end", values=row)
            for row in jobTable:
                tv5.insert("", "end", values=row)
            for row in computerTable:
                tv5.insert("", "end", values=row)
        populate(self)