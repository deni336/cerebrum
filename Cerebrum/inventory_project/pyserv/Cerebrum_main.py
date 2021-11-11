from re import L
import re
import sqlite3, os
from sqlite3 import Error
from flask import Flask, g
from flask_restful import Resource, Api
import pandas as pd
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from tkinter import ttk, Menu, font 
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk, Image

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#4b4b4b",
                "fg": "blue", "font": ("Arial", 12, "bold")}

database = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventory.db"

camera_table = []

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)    


class ProcessControl():
    def __init__(self) -> None:
        pass

    def create_database(self):
        conn = create_connection(database)    
        cur = conn.cursor()
        camera_table = '''CREATE TABLE IF NOT EXISTS CAMERA
        (ID INT PRIMARY KEY NOT NULL,
        MODEL TEXT NOT NULL,
        SERIAL_NUMBER TEXT NOT NULL,
        MAC_ADDRESS TEXT NOT NULL,
        IS_AVAILABLE TEXT NOT NULL,
        CHECK_OUT_DATE TEXT NOT NULL,
        CHECK_IN_DATE TEXT NOT NULL,
        CAMERA_LOCATION TEXT NOT NULL,
        WHO_HAS TEXT NOT NULL,
        CAMERA_PASS TEXT NOT NULL,
        PRICE TEXT NOT NULL);'''        
        computer_table = '''CREATE TABLE IF NOT EXISTS COMPUTER
        (ID INT PRIMARY KEY NOT NULL,
        PROCESSOR TEXT NOT NULL,
        MODEL TEXT NOT NULL,
        SERVICE_TAG TEXT NOT NULL,
        RAM TEXT NOT NULL,
        PRICE INT NOT NULL);'''                
        job_table = '''CREATE TABLE IF NOT EXISTS JOB
        (JOB_NUMBER INT PRIMARY KEY NOT NULL,
        COMPANY TEXT NOT NULL,
        CAMERA_TYPE TEXT NOT NULL,
        CAMERA_COUNT INT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ACCESSORIES TEXT NOT NULL,
        SOFTWARE_MODULES TEXT NOT NULL,
        PURCHASE_DATE TEXT NOT NULL,
        ARRIVAL_DATE TEXT NOT NULL,
        ITEM_APPLICATION TEXT NOT NULL,
        TESTING_STATUS TEXT NOT NULL,
        INFO TEXT);'''        
        worker_table = '''CREATE TABLE IF NOT EXISTS WORKER
        (ID INT PRIMARY KEY NOT NULL,
        WORKER_NAME TEXT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ITEMS TEXT NOT NULL);'''        
        cur.execute(computer_table)
        print("Computer table created successfully")
        cur.execute(job_table)
        print("Jobs table created successfully")
        cur.execute(worker_table)
        print("Workers table created successfully")
        cur.execute(camera_table)
        print("Camera table created successfully")
        conn.commit()
        conn.close()

    def create_camera(camera):
        conn = create_connection(database)
        try:
            sql = '''INSERT INTO camera (ID, MODEL,
                    SERIAL_NUMBER, MAC_ADDRESS, IS_AVAILABLE,
                    CHECK_OUT_DATE, CHECK_IN_DATE, CAMERA_LOCATION,
                    WHO_HAS, CAMERA_PASS, PRICE) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, camera)
            conn.commit()
            conn.close()
            print("Camera added successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def create_job(job):
        conn = create_connection(database)
        try:
            sql = '''INSERT INTO job (JOB_NUMBER, COMPANY,
                    CAMERA_TYPE, CAMERA_COUNT, CAMERAS, ACCESSORIES,
                    SOFTWARE_MODULES, PURCHASE_DATE, ARRIVAL_DATE,
                    ITEM_APPLICATION, TESTING_STATUS, INFO) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, job)
            conn.commit()
            conn.close()
            print("Job added successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def create_worker(worker):
        conn = create_connection(database)
        try:
            sql = '''INSERT INTO worker (ID, WORKER_NAME, CAMERAS, ITEMS) 
                    VALUES (?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, worker)
            conn.commit()
            conn.close()
            print("Worker added successfully")
        except Error as e:
            print(e)    
        return cur.lastrowid

    def create_computer(computer):
        conn = create_connection(database)
        try:
            sql = '''INSERT INTO computer (ID, PROCESSOR, MODEL,
                    SERVICE_TAG, RAM, PRICE) 
                    VALUES (?,?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, computer)
            conn.commit()
            conn.close()
            print("Computer added successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def update_camera(updateColumn, setValue, updateIndex):
        conn = create_connection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE CAMERA SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Camera updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def update_job(updateColumn, setValue, updateIndex):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE Job SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Job updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def update_worker(updateColumn, setValue, updateIndex):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE WORKER SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Worker updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def update_computer(updateColumn, setValue, updateIndex):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE COMPUTER SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Computer updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def read_camera(searchColumn, searchValue):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            read = cur.execute('SELECT * FROM CAMERA WHERE [{0}] = ?'.format(searchColumn) (searchValue))
            conn.close()
            print(read)
        except Error as e:
            print(e)
        

    def read_job(searchColumn, searchValue):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            read = cur.execute('SELECT * FROM CAMERA WHERE [{0}] = ?'.format(searchColumn), (searchValue))
            conn.close()
            Inventory_page.loadSearch
        except Error as e:
            print(e)
        return read

    def read_worker(searchColumn, searchValue):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            read = cur.execute('SELECT * FROM CAMERA WHERE [{0}] = ?'.format(searchColumn), (searchValue))
            conn.close()
        except Error as e:
            print(e)
        return read

    def read_computer(searchColumn, searchValue):
        conn = create_connection(database)
        try:            
            cur = conn.cursor()
            read = cur.execute('SELECT * FROM CAMERA WHERE [{0}] = ?'.format(searchColumn), (searchValue))
            conn.close()
        except Error as e:
            print(e)
        return read

    def delete_camera(dcamera):
        conn = create_connection(database)
        try:
            sql = '''DELETE FROM CAMERA
                    WHERE ID = ?'''
            cur = conn.cursor()
            cur.execute(sql, (dcamera))
            conn.commit()
            conn.close()
            print("Camera deleted successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def delete_job(djob):
        conn = create_connection(database)
        try:
            sql = '''DELETE FROM job
                    WHERE ID = (?)'''
            cur = conn.cursor()
            cur.execute(sql, djob)
            conn.commit()
            conn.close()
            print("Job deleted successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def delete_worker(dworker):
        conn = create_connection(database)
        try:
            sql = '''DELETE FROM worker
                    WHERE ID = (?)'''
            cur = conn.cursor()
            cur.execute(sql, dworker)
            conn.commit()
            conn.close()
            print("Worker deleted successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def delete_computer(dcomputer):
        conn = create_connection(database)
        try:
            sql = '''DELETE FROM computer
                    WHERE ID = (?)'''
            cur = conn.cursor()
            cur.execute(sql, dcomputer)
            conn.commit()
            conn.close()
            print("Computer deleted successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    table = ['camera', 'A65']

    def view_camera_table():
        conn = create_connection(database)
        sql = '''SELECT *
                FROM camera '''
        cur = conn.cursor()
        camera_table = []
        for row in cur.execute(sql):
            camera_table.append(row)            
        conn.close()
        return camera_table

    def view_worker_table():
        conn = create_connection(database)
        sql = '''SELECT *
                FROM worker '''
        cur = conn.cursor()
        worker_table = []
        for row in cur.execute(sql):
            worker_table.append(row)            
        conn.close()
        return worker_table

    def view_computer_table():
        conn = create_connection(database)
        sql = '''SELECT *
                FROM computer '''
        cur = conn.cursor()
        computer_table = []
        for row in cur.execute(sql):
            computer_table.append(row)            
        conn.close()
        return computer_table

    def view_job_table():
        conn = create_connection(database)
        sql = '''SELECT *
                FROM job '''
        cur = conn.cursor()
        job_table = []
        for row in cur.execute(sql):
            job_table.append(row)            
        conn.close()
        return job_table

    def view_readme():        
        os.system("start "+"C:\\Projects\\python_projects\\cerebrum\\readme.md")

class LoginPage(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#4b4b4b", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Arial", 16), "background": "#4b4b4b", "foreground": "blue"}

        text_styles = {"font": ("Arial", 14),
                       "background": "#4b4b4b",
                       "foreground": "blue"}

        frame_login = tk.Frame(main_frame, bg="#4b4b4b", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.75)

        def get_signup():
            SignupPage()

        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            # if your want to run the script as it is set validation = True
            validation = validate(username, password)
            if validation:
                tk.messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                root.deiconify()
                top.destroy()
            else:
                tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

        def validate(username, password):
            # Checks the text file for a username/password combination.
            try:
                with open("credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                print("You need to Register first or amend Line 71 to     if True:")
                return False

class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#4b4b4b", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Arial", 10),
                       "background": "#4b4b4b",
                       "foreground": "#E1FFFF"}

        label_user = tk.Label(main_frame, text_styles, text="New Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
            # Creates a text file with the Username and password
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if not validation:
                tk.messagebox.showerror("Information", "That Username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    tk.messagebox.showinfo("Information", "Your account details have been stored.")
                    SignupPage.destroy(self)

                else:
                    tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")

        def validate_user(username):
            # Checks the text file for a username/password combination.
            try:
                with open("credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu", menu=menu_file)
        menu_file.add_command(label="Welcome", command=lambda: parent.show_frame(Welcome_page))
        menu_file.add_command(label="Inventory Control", command=lambda: parent.show_frame(Inventory_page))
        menu_file.add_command(label="Visual", command=lambda: parent.show_frame(Visual_page))
        menu_file.add_command(label="Reports", command=lambda: parent.show_frame(Reports_page))
        menu_file.add_command(label="Admin", command=lambda: parent.show_frame(Admin_page))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)
        help_file.add_command(label="ReadMe", command=lambda: ProcessControl.view_readme())

        

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        self.geometry("1024x600") #fixes the applications size
        self.frames = {}
        pages = (Inventory_page, Welcome_page, Reports_page, Visual_page, Admin_page)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Inventory_page)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def Quit_application(self):
        self.destroy()

class GUI(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

class OpenNewWindow(GUI):

    def __init__(self, *args, **kwargs):
        
            tk.Tk.__init__(self, *args, **kwargs)

            main_frame = tk.Frame(self)
            main_frame.pack_propagate(0)
            main_frame.pack(fill="both", expand="true")
            main_frame.grid_rowconfigure(0, weight=1)
            main_frame.grid_columnconfigure(0, weight=1)
            self.title("Here is the Title of the Window")
            self.geometry("800x800")
            self.resizable(0, 0)


class Welcome_page(GUI):

    def __init__(self, parent, controller):

        GUI.__init__(self, parent)
        
        label1 = tk.Label(self.main_frame, font=("Arial", 20), text="Welcome", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")

        frame1 = tk.Frame(self, background="#4b4b4b")
        frame1.place(rely=0.05, relx=0.02, height=600, width=800)
        frame2 = tk.LabelFrame(self, frame_styles, text="System Info")
        frame2.place(rely=0.05, relx=0.68, height=600, width=400)


class Inventory_page(GUI):  # inherits from the GUI class

    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Arial", 20), text="Inventory", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.main_frame, frame_styles, text="Camera Database Output")
        frame1.place(rely=0.05, relx=0.02, height=200, width=800)
        frame2 = tk.LabelFrame(self.main_frame, frame_styles, text="Selected Item Display")
        frame2.place(rely=0.05, relx=0.85, height=600, width=200)
        frame3 = tk.LabelFrame(self.main_frame, frame_styles, text="Worker Database Output")
        frame3.place(rely=0.25, relx=0.02, height=200, width=800)
        frame4 = tk.LabelFrame(self.main_frame, frame_styles, text="Job Database Output")
        frame4.place(rely=0.45, relx=0.02, height=200, width=800)
        frame5 = tk.LabelFrame(self.main_frame, frame_styles, text="Computer Database Output")
        frame5.place(rely=0.65, relx=0.02, height=200, width=800)

        button1 = ttk.Button(self.main_frame, text="Populate All from Database", command=lambda: load_data())
        button1.place(rely=0.07, relx=0.75)        
        button2 = ttk.Button(self.main_frame, text="Clear Table", command=lambda: clear_data())
        button2.place(rely=0.10, relx=0.75)        
        button3 = ttk.Button(self.main_frame, text="Refresh Data", command=lambda: refresh_data())
        button3.place(rely=0.10, relx=0.79)
                
        button4 = ttk.Button(self.main_frame, text="Add Camera", command=lambda: addCameraFrame())
        button4.place(rely=0.07, relx=0.45)
        
        def addCameraFrame():
            
            framebtn4 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Camera Data")
            framebtn4.place(rely=0.66, relx=0.54, height=200, width=800)
            
            modelvar = Entry(framebtn4)
            modelvar.insert(END, "Camera Model")
            modelvar.place(rely=0.05, relx=0.01)
            
            serialvar = Entry(framebtn4)
            serialvar.insert(END, "Serial Number")
            serialvar.place(rely=0.20, relx=0.01)
            
            macvar = Entry(framebtn4)
            macvar.insert(END, "MAC Address")
            macvar.place(rely=0.34, relx=0.01)
            
            availvar = Entry(framebtn4)
            availvar.insert(END, "Is Camera Available?")
            availvar.place(rely=0.05, relx=0.20)
            
            dateoutvar = Entry(framebtn4)
            dateoutvar.insert(END, "Date Checked Out")
            dateoutvar.place(rely=0.48, relx=0.01)
            
            dateinvar = Entry(framebtn4)
            dateinvar.insert(END, "Date Checked In")
            dateinvar.place(rely=0.20, relx=0.20)
            
            cameralocvar = Entry(framebtn4)
            cameralocvar.insert(END, "Camera Location")
            cameralocvar.place(rely=0.34, relx=0.20)
            
            whohasvar = Entry(framebtn4)
            whohasvar.insert(END, "Who Has Camera?")
            whohasvar.place(rely=0.48, relx=0.20)
            
            camerapassvar = Entry(framebtn4)
            camerapassvar.insert(END, "Camera Password")
            camerapassvar.place(rely=0.05, relx=0.40)
            
            pricevar = Entry(framebtn4)
            pricevar.insert(END, "Price")
            pricevar.place(rely=0.20, relx=0.40)
            
            idvar = Entry(framebtn4)
            idvar.insert(END, "Database ID")
            idvar.place(rely=0.34, relx=0.40)
            
            writebtn = ttk.Button(framebtn4, text="Submit", command=lambda: loadCamCreateField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn4, text="Close", command=lambda: framebtn4.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadCamCreateField():
                modelvarg = modelvar.get()
                serialvarg = serialvar.get()
                macvarg = macvar.get()
                availvarg = availvar.get()
                dateoutvarg = dateoutvar.get()
                dateinvarg = dateinvar.get()
                cameralocvarg = cameralocvar.get()
                whohasvarg = whohasvar.get()
                camerapassvarg = camerapassvar.get()
                pricevarg = pricevar.get()
                idvarg = idvar.get()            
                addcam = [idvarg, modelvarg, serialvarg, macvarg, availvarg, dateoutvarg, dateinvarg, cameralocvarg, whohasvarg, camerapassvarg, pricevarg]
                ProcessControl.create_camera(addcam)            
            
        button5 = ttk.Button(self.main_frame, text="Add Worker", command=lambda: addWorkerFrame())
        button5.place(rely=0.27, relx=0.45)
        
        def addWorkerFrame():
            framebtn5 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Worker Data")
            framebtn5.place(rely=0.66, relx=0.54, height=200, width=800)
            
            idvar = Entry(framebtn5)
            idvar.insert(END, "Worker ID")
            idvar.place(rely=0.05, relx=0.01)
            
            workernamevar = Entry(framebtn5)
            workernamevar.insert(END, "Worker Name")
            workernamevar.place(rely=0.20, relx=0.01)
            
            wkrcamvar = Entry(framebtn5)
            wkrcamvar.insert(END, "Cameras in use")
            wkrcamvar.place(rely=0.34, relx=0.01)
            
            itemsvar = Entry(framebtn5)
            itemsvar.insert(END, "Items in use")
            itemsvar.place(rely=0.48, relx=0.01)            
            
            writebtn = ttk.Button(framebtn5, text="Submit", command=lambda: loadWorkerCreateField()) 
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn5, text="Close", command=lambda: framebtn5.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadWorkerCreateField():
                idvarg = idvar.get()
                workernamevarg = workernamevar.get()
                wkrcamvarg = wkrcamvar.get()
                itemsvarg = itemsvar.get()
                addworker = [idvarg, workernamevarg, wkrcamvarg, itemsvarg]
                ProcessControl.create_worker(addworker)
                
        button6 = ttk.Button(self.main_frame, text="Add Job", command=lambda: addJobFrame())
        button6.place(rely=0.47, relx=0.45)
        
        def addJobFrame():
            framebtn6 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Job Data")
            framebtn6.place(rely=0.66, relx=0.54, height=200, width=800)
            
            jobnumvar = Entry(framebtn6)
            jobnumvar.insert(END, "Job Number")
            jobnumvar.place(rely=0.05, relx=0.01)
            
            companyvar = Entry(framebtn6)
            companyvar.insert(END, "Company")
            companyvar.place(rely=0.20, relx=0.01)
            
            camtypevar = Entry(framebtn6)
            camtypevar.insert(END, "Camera Type")
            camtypevar.place(rely=0.34, relx=0.01)
            
            camcountvar = Entry(framebtn6)
            camcountvar.insert(END, "Camera Count")
            camcountvar.place(rely=0.48, relx=0.01)
            
            camservar = Entry(framebtn6)
            camservar.insert(END, "Camera Serial Numbers")
            camservar.place(rely=0.05, relx=0.20)
            
            accvar = Entry(framebtn6)
            accvar.insert(END, "Accessories")
            accvar.place(rely=0.20, relx=0.20)
            
            softmodvar = Entry(framebtn6)
            softmodvar.insert(END, "Software Modules")
            softmodvar.place(rely=0.34, relx=0.20)
            
            purdatevar = Entry(framebtn6)
            purdatevar.insert(END, "Purchase Date")
            purdatevar.place(rely=0.48, relx=0.20)
            
            arrdatevar = Entry(framebtn6)
            arrdatevar.insert(END, "Need By Date")
            arrdatevar.place(rely=0.05, relx=0.39)
            
            itmappvar = Entry(framebtn6)
            itmappvar.insert(END, "Job Application")
            itmappvar.place(rely=0.20, relx=0.39)
            
            teststatvar = Entry(framebtn6)
            teststatvar.insert(END, "Testing Status")
            teststatvar.place(rely=0.34, relx=0.39)
            
            infovar = Entry(framebtn6)
            infovar.insert(END, "Info")
            infovar.place(rely=0.48, relx=0.39)
            
            
            writebtn = ttk.Button(framebtn6, text="Submit", command=lambda: loadJobCreateField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn6, text="Close", command=lambda: framebtn6.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadJobCreateField():
                jobnumvarg = jobnumvar.get()
                companyvarg = companyvar.get()
                camtypevarg = camtypevar.get()
                camcountvarg = camcountvar.get()
                camservarg = camservar.get()
                accvarg = accvar.get()
                softmodvarg = softmodvar.get()
                purdatevarg = purdatevar.get()
                arrdatevarg = arrdatevar.get()
                itmappvarg = itmappvar.get()
                teststatvarg = teststatvar.get()
                infovarg = infovar.get()
            
                addjob = [jobnumvarg, companyvarg, camtypevarg, camcountvarg, camservarg, accvarg, softmodvarg, purdatevarg, arrdatevarg, itmappvarg, teststatvarg, infovarg]
                ProcessControl.create_job(addjob)
                
        button7 = ttk.Button(self.main_frame, text="Add Comp", command=lambda: createComputerFrame())
        button7.place(rely=0.67, relx=0.45)

        def createComputerFrame():
            framebtn7 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Computer Data")
            framebtn7.place(rely=0.66, relx=0.54, height=200, width=800)
            
            idvar = Entry(framebtn7)
            idvar.insert(END, "Computer ID")
            idvar.place(rely=0.05, relx=0.01)
            
            procvar = Entry(framebtn7)
            procvar.insert(END, "Processor")
            procvar.place(rely=0.20, relx=0.01)
            
            modvar = Entry(framebtn7)
            modvar.insert(END, "Computer Model")
            modvar.place(rely=0.34, relx=0.01)
            
            sertagvar = Entry(framebtn7)
            sertagvar.insert(END, "Service Tag")
            sertagvar.place(rely=0.48, relx=0.01)
            
            ramvar = Entry(framebtn7)
            ramvar.insert(END, "RAM")
            ramvar.place(rely=0.05, relx=0.20)
            
            pricevar = Entry(framebtn7)
            pricevar.insert(END, "Price")
            pricevar.place(rely=0.20, relx=0.20)
            
            
            writebtn = ttk.Button(framebtn7, text="Submit", command=lambda: loadComputerCreateField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn7, text="Close", command=lambda: framebtn7.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadComputerCreateField():
                idvarg = idvar.get()
                procvarg = procvar.get()
                modvarg = modvar.get()
                sertagvarg = sertagvar.get()
                ramvarg = ramvar.get()
                pricevarg = pricevar.get()
                addcomp = [idvarg, procvarg, modvarg, sertagvarg, ramvarg, pricevarg]
                ProcessControl.create_computer(addcomp)

        button8 = ttk.Button(self.main_frame, text="Update Camera", command=lambda: updateCameraFrame())
        button8.place(rely=0.13, relx=0.45)
        
        def updateCameraFrame():
            framebtn8 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Items to Change")
            framebtn8.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colvar = Entry(framebtn8)
            colvar.insert(END, "Column to Change")
            colvar.place(rely=0.05, relx=0.01)
            
            upitmvar = Entry(framebtn8)
            upitmvar.insert(END, "New Data")
            upitmvar.place(rely=0.20, relx=0.01)            
            
            whereitemvar = Entry(framebtn8)
            whereitemvar.insert(END, "Enter Item to searched")
            whereitemvar.place(rely=0.34, relx=0.01)            
            
            writebtn = ttk.Button(framebtn8, text="Submit", command=lambda: loadUpdateCameraField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn8, text="Close", command=lambda: framebtn8.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateCameraField():
                updateColumn = colvar.get()
                setValue = upitmvar.get()                
                updateIndex = whereitemvar.get()                
                ProcessControl.update_camera(updateColumn, setValue, updateIndex)
            
        button9 = ttk.Button(self.main_frame, text="Update Worker", command=lambda: ProcessControl.update_worker())
        button9.place(rely=0.30, relx=0.45)
        
        def updateCameraFrame():
            framebtn9 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Items to Change")
            framebtn9.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colvar = Entry(framebtn9)
            colvar.insert(END, "Column to Change")
            colvar.place(rely=0.05, relx=0.01)
            
            upitmvar = Entry(framebtn9)
            upitmvar.insert(END, "New Data")
            upitmvar.place(rely=0.20, relx=0.01)            
            
            whereitemvar = Entry(framebtn9)
            whereitemvar.insert(END, "Enter Item ID")
            whereitemvar.place(rely=0.34, relx=0.01)            
            
            writebtn = ttk.Button(framebtn9, text="Submit", command=lambda: loadUpdateCameraField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn9, text="Close", command=lambda: framebtn9.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateCameraField():
                updateColumn = colvar.get()
                setValue = upitmvar.get()                
                updateIndex = whereitemvar.get()                
                ProcessControl.update_camera(updateColumn, setValue, updateIndex)
                
        button10 = ttk.Button(self.main_frame, text="Update Job", command=lambda: updateJobFrame())
        button10.place(rely=0.50, relx=0.45)
        
        def updateJobFrame():
            framebtn10 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Items to Change")
            framebtn10.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colvar = Entry(framebtn10   )
            colvar.insert(END, "Column to Change")
            colvar.place(rely=0.05, relx=0.01)
            
            upitmvar = Entry(framebtn10)
            upitmvar.insert(END, "New Data")
            upitmvar.place(rely=0.20, relx=0.01)            
            
            whereitemvar = Entry(framebtn10)
            whereitemvar.insert(END, "Enter Item ID")
            whereitemvar.place(rely=0.34, relx=0.01)            
            
            writebtn = ttk.Button(framebtn10, text="Submit", command=lambda: loadUpdateJobField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn10, text="Close", command=lambda: framebtn10.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateJobField():
                updateColumn = colvar.get()
                setValue = upitmvar.get()                
                updateIndex = whereitemvar.get()                
                ProcessControl.update_job(updateColumn, setValue, updateIndex)
                
        button11 = ttk.Button(self.main_frame, text="Update Comp", command=lambda: updateComputerFrame())
        button11.place(rely=0.70, relx=0.45)
        
        def updateComputerFrame():
            framebtn11 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Items to Change")
            framebtn11.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colvar = Entry(framebtn11)
            colvar.insert(END, "Column to Change")
            colvar.place(rely=0.05, relx=0.01)
            
            upitmvar = Entry(framebtn11)
            upitmvar.insert(END, "New Data")
            upitmvar.place(rely=0.20, relx=0.01)            
            
            whereitemvar = Entry(framebtn11)
            whereitemvar.insert(END, "Enter Item to searched")
            whereitemvar.place(rely=0.34, relx=0.01)            
            
            writebtn = ttk.Button(framebtn11, text="Submit", command=lambda: loadUpdateComputerField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn11, text="Close", command=lambda: framebtn11.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateComputerField():
                updateColumn = colvar.get()
                setValue = upitmvar.get()                
                updateIndex = whereitemvar.get()                
                ProcessControl.update_computer(updateColumn, setValue, updateIndex)
                
        button12 = ttk.Button(self.main_frame, text="Search Camera", command=lambda: searchCameraFrame())
        button12.place(rely=0.10, relx=0.45)
        
        def searchCameraFrame():
            framebtn12 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Search Data")
            framebtn12.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchvar1 = Entry(framebtn12)
            searchvar1.insert(END, "Enter Column to Search by")
            searchvar1.place(rely=0.05, relx=0.01)
            
            searchvar2 = Entry(framebtn12)
            searchvar2.insert(END, "Enter Search Value")
            searchvar2.place(rely=0.20, relx=0.01)
            
            writebtn = ttk.Button(framebtn12, text="Submit", command=lambda: loadSearchCameraField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn12, text="Close", command=lambda: framebtn12.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadSearchCameraField():
                searchColumn = searchvar1.get()
                searchValue = searchvar2.get()
                ProcessControl.read_camera(searchColumn, searchValue)        
            
        button13 = ttk.Button(self.main_frame, text="Search Worker", command=lambda: searchWorkerFrame())
        button13.place(rely=0.33, relx=0.45)
        
        def searchWorkerFrame():
            framebtn13 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Search Data")
            framebtn13.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchvar1 = Entry(framebtn13)
            searchvar1.insert(END, "Enter Column to Search by")
            searchvar1.place(rely=0.05, relx=0.01)
            
            searchvar2 = Entry(framebtn13)
            searchvar2.inser(END, "Enter Search Value")
            searchvar2.place(rely=0.20, relx=0.01)
            
            writebtn = ttk.Button(framebtn13, text="Submit", command=lambda: loadSearchWorkerField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn13, text="Close", command=lambda: framebtn13.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadSearchWorkerField():
                searchColumn = searchvar1.get()
                searchValue = searchvar2.get()
                ProcessControl.read_worker(searchColumn, searchValue)
                
        button14 = ttk.Button(self.main_frame, text="Search Job", command=lambda: searchJobFrame())
        button14.place(rely=0.53, relx=0.45)
        
        def searchJobFrame():
            framebtn14 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Search Data")
            framebtn14.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchvar1 = Entry(framebtn14)
            searchvar1.insert(END, "Enter Column to Search by")
            searchvar1.place(rely=0.05, relx=0.01)
            
            searchvar2 = Entry(framebtn14)
            searchvar2.inser(END, "Enter Search Value")
            searchvar2.place(rely=0.20, relx=0.01)
            
            writebtn = ttk.Button(framebtn14, text="Submit", command=lambda: loadSearchJobField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn14, text="Close", command=lambda: framebtn14.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadSearchJobField():
                searchColumn = searchvar1.get()
                searchValue = searchvar2.get()
                ProcessControl.read_job(searchColumn, searchValue)
                
        button15 = ttk.Button(self.main_frame, text="Search Comp", command=lambda: searchComputerFrame())
        button15.place(rely=0.73, relx=0.45)
        
        def searchComputerFrame():
            framebtn15 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Search Data")
            framebtn15.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchvar1 = Entry(framebtn15)
            searchvar1.insert(END, "Enter Column to Search by")
            searchvar1.place(rely=0.05, relx=0.01)
            
            searchvar2 = Entry(framebtn15)
            searchvar2.inser(END, "Enter Search Value")
            searchvar2.place(rely=0.20, relx=0.01)
            
            writebtn = ttk.Button(framebtn15, text="Submit", command=lambda: loadSearchComputerField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn15, text="Close", command=lambda: framebtn15.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadSearchComputerField():
                searchColumn = searchvar1.get()
                searchValue = searchvar2.get()
                ProcessControl.read_computer(searchColumn, searchValue)                
        
        button16 = ttk.Button(self.main_frame, text="Delete Camera", command=lambda: delCamFrame())
        button16.place(rely=0.16, relx=0.45)
        
        def delCamFrame():
            framebtn16 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Item to Delete")
            framebtn16.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delidvar = Entry(framebtn16)
            delidvar.insert(END, "Enter ID to be Deleted")
            delidvar.place(rely=0.05, relx=0.01)            
            
            writebtn = ttk.Button(framebtn16, text="Submit", command=lambda: loadCamDeleteField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn16, text="Close", command=lambda: framebtn16.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadCamDeleteField():
                delidvarg = delidvar.get()
                delcam = [delidvarg]
                ProcessControl.delete_camera(delcam)
                
        button17 = ttk.Button(self.main_frame, text="Delete Worker", command=lambda: delWorkerFrame())
        button17.place(rely=0.36, relx=0.45)
        
        def delWorkerFrame():
            framebtn17 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Item to Delete")
            framebtn17.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delidvar = Entry(framebtn17)
            delidvar.insert(END, "Enter ID to be Deleted")
            delidvar.place(rely=0.05, relx=0.01)            
            
            writebtn = ttk.Button(framebtn17, text="Submit", command=lambda: loadWorkerDeleteField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn17, text="Close", command=lambda: framebtn17.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadWorkerDeleteField():
                delidvarg = delidvar.get()
                delwkr = [delidvarg]
                ProcessControl.delete_worker(delwkr)
                
        button18 = ttk.Button(self.main_frame, text="Delete Job", command=lambda: delJobFrame())
        button18.place(rely=0.56, relx=0.45)
        
        def delJobFrame():
            framebtn18 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Item to Delete")
            framebtn18.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delidvar = Entry(framebtn18)
            delidvar.insert(END, "Enter ID to be Deleted")
            delidvar.place(rely=0.05, relx=0.01)            
            
            writebtn = ttk.Button(framebtn18, text="Submit", command=lambda: loadJobDeleteField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn18, text="Close", command=lambda: framebtn18.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadJobDeleteField():
                delidvarg = delidvar.get()
                deljob = [delidvarg]
                ProcessControl.delete_job(deljob)
                
        button19 = ttk.Button(self.main_frame, text="Delete Computer", command=lambda: delComputerFrame())
        button19.place(rely=0.76, relx=0.45)
        
        def delComputerFrame():
            framebtn19 = tk.LabelFrame(self.main_frame, frame_styles, text="Input Item to Delete")
            framebtn19.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delidvar = Entry(framebtn19)
            delidvar.insert(END, "Enter ID to be Deleted")
            delidvar.place(rely=0.05, relx=0.01)
            
            
            writebtn = ttk.Button(framebtn19, text="Submit", command=lambda: loadComputerDeleteField())
            writebtn.place(rely=0.80, relx=0.77)
            closebtn = ttk.Button(framebtn19, text="Close", command=lambda: framebtn19.destroy())
            closebtn.place(rely=0.80, relx=0.87)
            
            def loadComputerDeleteField():
                delidvarg = delidvar.get()
                delcomp = [delidvarg]
                ProcessControl.delete_computer(delcomp)
                
                        
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["ID", "Model", "Serial", "Mac Address", "Is Available", "Check Out Date", "Check In Date","Camera Location", "Who Has", "Camera Password", "Price"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=.995)
        treescrolly = tk.Scrollbar(frame1)
        treescrolly.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescrolly.set)
        treescrolly.pack(side="right", fill="y")

        tv2 = ttk.Treeview(frame3)
        column_list_account = ["ID", "Name", "Cameras in use", "Items in use"]
        tv2['columns'] = column_list_account
        tv2["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv2.heading(column, text=column)
            tv2.column(column, width=50)
        tv2.place(relheight=1, relwidth=.995)
        treescrolly = tk.Scrollbar(frame3)
        treescrolly.configure(command=tv2.yview)
        tv2.configure(yscrollcommand=treescrolly.set)
        treescrolly.pack(side="right", fill="y")

        tv3 = ttk.Treeview(frame4)
        column_list_account = ["Job Number", "Company", "Camera Type", "Camera Count", "Camera Serials", "Accessories", "Software Modules", "Purchase Date", "Need by Date", "Job Application", "Testing Status", "Info"]
        tv3['columns'] = column_list_account
        tv3["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv3.heading(column, text=column)
            tv3.column(column, width=50)
        tv3.place(relheight=1, relwidth=.995)
        treescrolly = tk.Scrollbar(frame4)
        treescrolly.configure(command=tv3.yview)
        tv3.configure(yscrollcommand=treescrolly.set)
        treescrolly.pack(side="right", fill="y")

        tv4 = ttk.Treeview(frame5)
        column_list_account = ["ID", "Processor", "Model", "Service Tag", "RAM", "Price"]
        tv4['columns'] = column_list_account
        tv4["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv4.heading(column, text=column)
            tv4.column(column, width=50)
        tv4.place(relheight=1, relwidth=.995)
        treescrolly = tk.Scrollbar(frame5)
        treescrolly.configure(command=tv4.yview)
        tv4.configure(yscrollcommand=treescrolly.set)
        treescrolly.pack(side="right", fill="y")
        
        
        def load_data():
            camera_table = ProcessControl.view_camera_table()
            worker_table = ProcessControl.view_worker_table()
            job_table = ProcessControl.view_job_table()
            computer_table = ProcessControl.view_computer_table()
            for row in camera_table:
                tv1.insert("", "end", values=row)
            for row in worker_table:
                tv2.insert("", "end", values=row)
            for row in job_table:
                tv3.insert("", "end", values=row)
            for row in computer_table:
                tv4.insert("", "end", values=row)
                

        def refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv4.delete(*tv4.get_children())
            load_data()
            
        
        def clear_data():
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv3.delete(*tv3.get_children())
        
        def displaySearchCamera(read):
            tv1.delete(tv1.get_children())
            for row in read:
                tv1.insert("", "end", values=row)

        


class Visual_page(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Arial", 20), text="Visual", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")
        

class Admin_page(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Arial", 20), text="Admin", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")
        button1 = ttk.Button(self.main_frame, text="Create Database", command=lambda: ProcessControl.create_database(self))
        button1.pack()


class Reports_page(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Arial", 20), text="Reports Viewer", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self, frame_styles, text="Report Left", background="#4b4b4b")
        frame1.place(rely=0.05, relx=0.02, height=600, width=500)
        frame2 = tk.LabelFrame(self, frame_styles, text="Report Right")
        frame2.place(rely=0.05, relx=0.60, height=600, width=500)

        button1 = tk.Button(self.main_frame, text="Inventory Report", command=lambda: quit())
        button1.place(rely=0.05, relx=0.5, height=10, width=25)
        button1.pack()
        button2 = tk.Button(self.main_frame, text="Purchase Orders", command=lambda: quit())
        button2.place(rely=0.1, relx=0.5, height=10, width=25)
        button2.pack()

top = LoginPage()
top.title("Cerebrum - Login Page")
root = MyApp()
app=FullScreenApp(root)
root.state('zoomed')
root.withdraw()
root.title("Cerebrum")

root.mainloop()

