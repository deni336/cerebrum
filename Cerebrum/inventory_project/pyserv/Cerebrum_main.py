import threading
import sqlite3, os
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from tkinter import ttk, Menu, font 
from tkinter.ttk import Progressbar
from tkinter import *
from itertools import cycle
from PIL import ImageTk, Image
import time



frameStyles = {"relief": "groove",
                "bd": 3, "bg": "#4b4b4b",
                "fg": "blue", "font": ("Arial", 12, "bold")}

database = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventory.db"
databaseBackup = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventorybackup.db"

def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)    


class ProcessControl():
    def __init__(self) -> None:
        pass

    def createDatabase(self):
        conn = createConnection(database)            
        cur = conn.cursor()
        cameraTable = '''CREATE TABLE IF NOT EXISTS CAMERA
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
        computerTable = '''CREATE TABLE IF NOT EXISTS COMPUTER
        (ID INT PRIMARY KEY NOT NULL,
        PROCESSOR TEXT NOT NULL,
        MODEL TEXT NOT NULL,
        SERVICE_TAG TEXT NOT NULL,
        RAM TEXT NOT NULL,
        PRICE INT NOT NULL);'''                
        jobTable = '''CREATE TABLE IF NOT EXISTS JOB
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
        workerTable = '''CREATE TABLE IF NOT EXISTS WORKER
        (ID INT PRIMARY KEY NOT NULL,
        WORKER_NAME TEXT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ITEMS TEXT NOT NULL);'''        
        cur.execute(computerTable)
        print("Computer table created successfully")
        cur.execute(jobTable)
        print("Jobs table created successfully")
        cur.execute(workerTable)
        print("Workers table created successfully")
        cur.execute(cameraTable)
        print("Camera table created successfully")
        conn.commit()
        conn.close()
        
    def createBackupDatabase(self):
        conn = createConnection(databaseBackup)            
        cur = conn.cursor()
        cameraTable = '''CREATE TABLE IF NOT EXISTS CAMERA
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
        computerTable = '''CREATE TABLE IF NOT EXISTS COMPUTER
        (ID INT PRIMARY KEY NOT NULL,
        PROCESSOR TEXT NOT NULL,
        MODEL TEXT NOT NULL,
        SERVICE_TAG TEXT NOT NULL,
        RAM TEXT NOT NULL,
        PRICE INT NOT NULL);'''                
        jobTable = '''CREATE TABLE IF NOT EXISTS JOB
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
        workerTable = '''CREATE TABLE IF NOT EXISTS WORKER
        (ID INT PRIMARY KEY NOT NULL,
        WORKER_NAME TEXT NOT NULL,
        CAMERAS TEXT NOT NULL,
        ITEMS TEXT NOT NULL);'''        
        cur.execute(computerTable)
        print("Computer table created successfully")
        cur.execute(jobTable)
        print("Jobs table created successfully")
        cur.execute(workerTable)
        print("Workers table created successfully")
        cur.execute(cameraTable)
        print("Camera table created successfully")
        conn.commit()
        conn.close()
        
    def backupDatabase():        
        try:
            conn = createConnection(database)
            conn.backup(createConnection(databaseBackup), pages=0, progress=None)
            conn.commit()
            conn.close()            
        except Error as e:
            return e            

    def createCamera(camera):
        conn = createConnection(database)
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

    def createJob(job):
        conn = createConnection(database)
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

    def createWorker(worker):
        conn = createConnection(database)
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

    def createComputer(computer):
        conn = createConnection(database)
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

    def updateCamera(updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:
            cur = conn.cursor()
            cur.execute('UPDATE CAMERA SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Camera updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateJob(updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE Job SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Job updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateWorker(updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE WORKER SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Worker updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def updateComputer(updateColumn, setValue, updateIndex):
        conn = createConnection(database)
        try:            
            cur = conn.cursor()
            cur.execute('UPDATE COMPUTER SET [{0}] = ? WHERE ID = ?'.format(updateColumn), (setValue, updateIndex))
            conn.commit()
            conn.close()
            print("Computer updated successfully")
        except Error as e:
            print(e)
        return cur.lastrowid

    def readCamera(searchColumn, searchValue):
        conn = createConnection(database)
        read = []        
        try:
            sql = 'SELECT * FROM CAMERA WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)            
            conn.close()
        except Error as e:
            print(e) 
        return read       

    def readJob(searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:            
            sql = 'SELECT * FROM JOB WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)            
            conn.close()
        except Error as e:
            print(e)
        return read

    def readWorker(searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:            
            sql = 'SELECT * FROM Worker WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)         
            conn.close()
        except Error as e:
            print(e)
        return read

    def readComputer(searchColumn, searchValue):
        conn = createConnection(database)
        read = []
        try:            
            sql = 'SELECT * FROM COMPUTER WHERE [{0}] = ?'
            cur = conn.cursor()
            reading = cur.execute(sql.format(searchColumn), (searchValue,))
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

    def deleteCamera(dcamera):
        conn = createConnection(database)
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

    def deleteJob(djob):
        conn = createConnection(database)
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

    def deleteWorker(dworker):
        conn = createConnection(database)
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

    def deleteComputer(dcomputer):
        conn = createConnection(database)
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

    def viewCameraTable():
        conn = createConnection(database)
        sql = '''SELECT *
                FROM camera '''
        cur = conn.cursor()
        cameraTable = []
        for row in cur.execute(sql):
            cameraTable.append(row)            
        conn.close()
        return cameraTable

    def viewWorkerTable():
        conn = createConnection(database)
        sql = '''SELECT *
                FROM worker '''
        cur = conn.cursor()
        workerTable = []
        for row in cur.execute(sql):
            workerTable.append(row)            
        conn.close()
        return workerTable

    def viewComputerTable():
        conn = createConnection(database)
        sql = '''SELECT *
                FROM computer '''
        cur = conn.cursor()
        computerTable = []
        for row in cur.execute(sql):
            computerTable.append(row)            
        conn.close()
        return computerTable

    def viewJobTable():
        conn = createConnection(database)
        sql = '''SELECT *
                FROM job '''
        cur = conn.cursor()
        jobTable = []
        for row in cur.execute(sql):
            jobTable.append(row)            
        conn.close()
        return jobTable

    def viewReadme():        
        os.system("start "+"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\readme.md")


#for later use
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
    
    

class LoginPage(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        mainFrame = tk.Frame(self, bg="#4b4b4b", height=431, width=626)  # this is the background
        mainFrame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Arial", 16), "background": "#4b4b4b", "foreground": "blue"}

        text_styles = {"font": ("Arial", 14),
                       "background": "#4b4b4b",
                       "foreground": "blue"}

        frameLogin = tk.Frame(mainFrame, bg="#4b4b4b", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frameLogin.place(rely=0.30, relx=0.17, height=130, width=400)

        labelTitle = tk.Label(frameLogin, title_styles, text="Login Page")
        labelTitle.grid(row=0, column=1, columnspan=1)

        labelUser = tk.Label(frameLogin, text_styles, text="Username:")
        labelUser.grid(row=1, column=0)

        labelPw = tk.Label(frameLogin, text_styles, text="Password:")
        labelPw.grid(row=2, column=0)

        entryUser = ttk.Entry(frameLogin, width=45, cursor="xterm")
        entryUser.grid(row=1, column=1)

        entryPw = ttk.Entry(frameLogin, width=45, cursor="xterm", show="*")
        entryPw.grid(row=2, column=1)

        button = ttk.Button(frameLogin, text="Login", command=lambda: getLogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frameLogin, text="Register", command=lambda: getSignup())
        signup_btn.place(rely=0.70, relx=0.75)

        def getSignup():
            SignupPage()

        def getLogin():
            username = entryUser.get()
            password = entryPw.get()
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

        mainFrame = tk.Frame(self, bg="#4b4b4b", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        mainFrame.pack_propagate(0)
        mainFrame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Arial", 10),
                       "background": "#4b4b4b",
                       "foreground": "#E1FFFF"}

        labelUser = tk.Label(mainFrame, text_styles, text="New Username:")
        labelUser.grid(row=1, column=0)

        labelPw = tk.Label(mainFrame, text_styles, text="New Password:")
        labelPw.grid(row=2, column=0)

        entryUser = ttk.Entry(mainFrame, width=20, cursor="xterm")
        entryUser.grid(row=1, column=1)

        entryPw = ttk.Entry(mainFrame, width=20, cursor="xterm", show="*")
        entryPw.grid(row=2, column=1)

        button = ttk.Button(mainFrame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
            # Creates a text file with the Username and password
            user = entryUser.get()
            pw = entryPw.get()
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
        #menu_file.add_command(label="Welcome", command=lambda: parent.showFrame(WelcomePage))
        menu_file.add_command(label="Inventory Control", command=lambda: parent.showFrame(InventoryPage))
        #menu_file.add_command(label="Visual", command=lambda: parent.showFrame(VisualPage))
        #menu_file.add_command(label="Reports", command=lambda: parent.showFrame(ReportsPage))
        menu_file.add_command(label="Admin", command=lambda: parent.showFrame(AdminPage))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.quitApplication())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)
        help_file.add_command(label="ReadMe", command=lambda: ProcessControl.viewReadme())

        

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
        mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        mainFrame.pack_propagate(0)
        mainFrame.pack(fill="both", expand="true")
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        self.geometry("1024x600") #fixes the applications size
        self.frames = {}
        pages = (InventoryPage, AdminPage)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(InventoryPage)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def quitApplication(self):
        self.destroy()

class GUI(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        # self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both", expand="true")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)

class OpenNewWindow(GUI):

    def __init__(self, *args, **kwargs):
        
            tk.Tk.__init__(self, *args, **kwargs)

            mainFrame = tk.Frame(self)
            mainFrame.pack_propagate(0)
            mainFrame.pack(fill="both", expand="true")
            mainFrame.grid_rowconfigure(0, weight=1)
            mainFrame.grid_columnconfigure(0, weight=1)
            self.title("Here is the Title of the Window")
            self.geometry("800x800")
            self.resizable(0, 0)


# class WelcomePage(GUI):

#     def __init__(self, parent, controller):

#         GUI.__init__(self, parent)
        
#         label1 = tk.Label(self.mainFrame, font=("Arial", 20), text="Welcome", background="#4b4b4b", foreground="blue")
#         label1.pack(side="top")

#         frame1 = tk.Frame(self, background="#4b4b4b")
#         frame1.place(rely=0.05, relx=0.02, height=600, width=800)
#         #images = ["CerebrumImage1.jpg", "CerebrumImage2.png", "CerebrumImage3.jpg"]
#         #photos = cycle(ImageTk.PhotoImage(Image.open(image))for image in images)
#         # imgLabel = Label(self, image="C:\\Projects\\Python_Projects\\cerebrum\\Cerebrum\\inventory_project\\pyserv\\CerebrumImage1.jpg")        
#         # imgLabel.place(rely=0.05, relx=0.68, height=600, width=400)


class InventoryPage(GUI):  # inherits from the GUI class

    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20), text="Inventory", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, frameStyles, text="Camera Database Output")
        frame1.place(rely=0.05, relx=0.02, height=200, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, frameStyles, text="Selected Item Display")
        frame2.place(rely=0.05, relx=0.85, height=600, width=200)
        frame3 = tk.LabelFrame(self.mainFrame, frameStyles, text="Worker Database Output")
        frame3.place(rely=0.25, relx=0.02, height=200, width=800)
        frame4 = tk.LabelFrame(self.mainFrame, frameStyles, text="Job Database Output")
        frame4.place(rely=0.45, relx=0.02, height=200, width=800)
        frame5 = tk.LabelFrame(self.mainFrame, frameStyles, text="Computer Database Output")
        frame5.place(rely=0.65, relx=0.02, height=200, width=800)

        button1 = ttk.Button(self.mainFrame, text="Populate All from Database", command=lambda: loadData())
        button1.place(rely=0.07, relx=0.75)        
        button2 = ttk.Button(self.mainFrame, text="Clear Table", command=lambda: clear_data())
        button2.place(rely=0.10, relx=0.75)        
        button3 = ttk.Button(self.mainFrame, text="Refresh Data", command=lambda: refreshData())
        button3.place(rely=0.10, relx=0.79)
                
        button4 = ttk.Button(self.mainFrame, text="Add Camera", command=lambda: addCameraFrame())
        button4.place(rely=0.07, relx=0.45)
        
        def addCameraFrame():
            
            frameBtn4 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Camera Data")
            frameBtn4.place(rely=0.66, relx=0.54, height=200, width=800)
            
            modelVar = Entry(frameBtn4)
            modelVar.insert(END, "Camera Model")
            modelVar.place(rely=0.05, relx=0.01)
            
            serialVar = Entry(frameBtn4)
            serialVar.insert(END, "Serial Number")
            serialVar.place(rely=0.20, relx=0.01)
            
            macVar = Entry(frameBtn4)
            macVar.insert(END, "MAC Address")
            macVar.place(rely=0.34, relx=0.01)
            
            availVar = Entry(frameBtn4)
            availVar.insert(END, "Is Camera Available?")
            availVar.place(rely=0.05, relx=0.20)
            
            dateOutVar = Entry(frameBtn4)
            dateOutVar.insert(END, "Date Checked Out")
            dateOutVar.place(rely=0.48, relx=0.01)
            
            dateInVar = Entry(frameBtn4)
            dateInVar.insert(END, "Date Checked In")
            dateInVar.place(rely=0.20, relx=0.20)
            
            cameraLocVar = Entry(frameBtn4)
            cameraLocVar.insert(END, "Camera Location")
            cameraLocVar.place(rely=0.34, relx=0.20)
            
            whoHasVar = Entry(frameBtn4)
            whoHasVar.insert(END, "Who Has Camera?")
            whoHasVar.place(rely=0.48, relx=0.20)
            
            cameraPassVar = Entry(frameBtn4)
            cameraPassVar.insert(END, "Camera Password")
            cameraPassVar.place(rely=0.05, relx=0.40)
            
            priceVar = Entry(frameBtn4)
            priceVar.insert(END, "Price")
            priceVar.place(rely=0.20, relx=0.40)
            
            idVar = Entry(frameBtn4)
            idVar.insert(END, "Database ID")
            idVar.place(rely=0.34, relx=0.40)
            
            writeBtn = ttk.Button(frameBtn4, text="Submit", command=lambda: loadCamCreateField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn4, text="Close", command=lambda: frameBtn4.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadCamCreateField():
                modelVarg = modelVar.get()
                serialVarg = serialVar.get()
                macVarg = macVar.get()
                availVarg = availVar.get()
                dateOutVarg = dateOutVar.get()
                dateInVarg = dateInVar.get()
                cameraLocVarg = cameraLocVar.get()
                whoHasVarg = whoHasVar.get()
                cameraPassVarg = cameraPassVar.get()
                priceVarg = priceVar.get()
                idVarg = idVar.get()            
                addCam = [idVarg, modelVarg, serialVarg, macVarg, availVarg, dateOutVarg, dateInVarg, cameraLocVarg, whoHasVarg, cameraPassVarg, priceVarg]
                ProcessControl.createCamera(addCam)            
            
        button5 = ttk.Button(self.mainFrame, text="Add Worker", command=lambda: addWorkerFrame())
        button5.place(rely=0.27, relx=0.45)
        
        def addWorkerFrame():
            frameBtn5 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Worker Data")
            frameBtn5.place(rely=0.66, relx=0.54, height=200, width=800)
            
            idVar = Entry(frameBtn5)
            idVar.insert(END, "Worker ID")
            idVar.place(rely=0.05, relx=0.01)
            
            wkrNameVar = Entry(frameBtn5)
            wkrNameVar.insert(END, "Worker Name")
            wkrNameVar.place(rely=0.20, relx=0.01)
            
            wkrCamVar = Entry(frameBtn5)
            wkrCamVar.insert(END, "Cameras in use")
            wkrCamVar.place(rely=0.34, relx=0.01)
            
            itmVar = Entry(frameBtn5)
            itmVar.insert(END, "Items in use")
            itmVar.place(rely=0.48, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn5, text="Submit", command=lambda: loadWorkerCreateField()) 
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn5, text="Close", command=lambda: frameBtn5.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadWorkerCreateField():
                idVarg = idVar.get()
                wkrNameVarg = wkrNameVar.get()
                wkrCamVarg = wkrCamVar.get()
                itmVarg = itmVar.get()
                addWorker = [idVarg, wkrNameVarg, wkrCamVarg, itmVarg]
                ProcessControl.createWorker(addWorker)
                
        button6 = ttk.Button(self.mainFrame, text="Add Job", command=lambda: addJobFrame())
        button6.place(rely=0.47, relx=0.45)
        
        def addJobFrame():
            frameBtn6 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Job Data")
            frameBtn6.place(rely=0.66, relx=0.54, height=200, width=800)
            
            jobNumVar = Entry(frameBtn6)
            jobNumVar.insert(END, "Job Number")
            jobNumVar.place(rely=0.05, relx=0.01)
            
            companyVar = Entry(frameBtn6)
            companyVar.insert(END, "Company")
            companyVar.place(rely=0.20, relx=0.01)
            
            camTypeVar = Entry(frameBtn6)
            camTypeVar.insert(END, "Camera Type")
            camTypeVar.place(rely=0.34, relx=0.01)
            
            camCountVar = Entry(frameBtn6)
            camCountVar.insert(END, "Camera Count")
            camCountVar.place(rely=0.48, relx=0.01)
            
            camSerVar = Entry(frameBtn6)
            camSerVar.insert(END, "Camera Serial Numbers")
            camSerVar.place(rely=0.05, relx=0.20)
            
            accVar = Entry(frameBtn6)
            accVar.insert(END, "Accessories")
            accVar.place(rely=0.20, relx=0.20)
            
            softModVar = Entry(frameBtn6)
            softModVar.insert(END, "Software Modules")
            softModVar.place(rely=0.34, relx=0.20)
            
            purDateVar = Entry(frameBtn6)
            purDateVar.insert(END, "Purchase Date")
            purDateVar.place(rely=0.48, relx=0.20)
            
            arrDateVar = Entry(frameBtn6)
            arrDateVar.insert(END, "Need By Date")
            arrDateVar.place(rely=0.05, relx=0.39)
            
            itmAppVar = Entry(frameBtn6)
            itmAppVar.insert(END, "Job Application")
            itmAppVar.place(rely=0.20, relx=0.39)
            
            testStatVar = Entry(frameBtn6)
            testStatVar.insert(END, "Testing Status")
            testStatVar.place(rely=0.34, relx=0.39)
            
            infoVar = Entry(frameBtn6)
            infoVar.insert(END, "Info")
            infoVar.place(rely=0.48, relx=0.39)
            
            
            writeBtn = ttk.Button(frameBtn6, text="Submit", command=lambda: loadJobCreateField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn6, text="Close", command=lambda: frameBtn6.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadJobCreateField():
                jobNumVarg = jobNumVar.get()
                companyVarg = companyVar.get()
                camTypeVarg = camTypeVar.get()
                camCountVarg = camCountVar.get()
                camSerVarg = camSerVar.get()
                accVarg = accVar.get()
                softModVarg = softModVar.get()
                purDateVarg = purDateVar.get()
                arrDateVarg = arrDateVar.get()
                itmAppVarg = itmAppVar.get()
                testStatVarg = testStatVar.get()
                infoVarg = infoVar.get()
            
                addJob = [jobNumVarg, companyVarg, camTypeVarg, camCountVarg, camSerVarg, accVarg, softModVarg, purDateVarg, arrDateVarg, itmAppVarg, testStatVarg, infoVarg]
                ProcessControl.createJob(addJob)
                
        button7 = ttk.Button(self.mainFrame, text="Add Comp", command=lambda: createComputerFrame())
        button7.place(rely=0.67, relx=0.45)

        def createComputerFrame():
            frameBtn7 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Computer Data")
            frameBtn7.place(rely=0.66, relx=0.54, height=200, width=800)
            
            idVar = Entry(frameBtn7)
            idVar.insert(END, "Computer ID")
            idVar.place(rely=0.05, relx=0.01)
            
            procVar = Entry(frameBtn7)
            procVar.insert(END, "Processor")
            procVar.place(rely=0.20, relx=0.01)
            
            modVar = Entry(frameBtn7)
            modVar.insert(END, "Computer Model")
            modVar.place(rely=0.34, relx=0.01)
            
            serTagVar = Entry(frameBtn7)
            serTagVar.insert(END, "Service Tag")
            serTagVar.place(rely=0.48, relx=0.01)
            
            ramVar = Entry(frameBtn7)
            ramVar.insert(END, "RAM")
            ramVar.place(rely=0.05, relx=0.20)
            
            priceVar = Entry(frameBtn7)
            priceVar.insert(END, "Price")
            priceVar.place(rely=0.20, relx=0.20)
            
            
            writeBtn = ttk.Button(frameBtn7, text="Submit", command=lambda: loadComputerCreateField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn7, text="Close", command=lambda: frameBtn7.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadComputerCreateField():
                idVarg = idVar.get()
                procVarg = procVar.get()
                modVarg = modVar.get()
                serTagVarg = serTagVar.get()
                ramVarg = ramVar.get()
                priceVarg = priceVar.get()
                addComp = [idVarg, procVarg, modVarg, serTagVarg, ramVarg, priceVarg]
                ProcessControl.createComputer(addComp)

        button8 = ttk.Button(self.mainFrame, text="Update Camera", command=lambda: updateCameraFrame())
        button8.place(rely=0.13, relx=0.45)
        
        def updateCameraFrame():
            frameBtn8 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Items to Change")
            frameBtn8.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colVar = Entry(frameBtn8)
            colVar.insert(END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)
            
            updItmVar = Entry(frameBtn8)
            updItmVar.insert(END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)            
            
            whereItmVar = Entry(frameBtn8)
            whereItmVar.insert(END, "Enter Item to searched")
            whereItmVar.place(rely=0.34, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn8, text="Submit", command=lambda: loadUpdateCameraField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn8, text="Close", command=lambda: frameBtn8.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateCameraField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()                
                updateIndex = whereItmVar.get()                
                ProcessControl.updateCamera(updateColumn, setValue, updateIndex)
            
        button9 = ttk.Button(self.mainFrame, text="Update Worker", command=lambda: updateWorkerFrame())
        button9.place(rely=0.30, relx=0.45)
        
        def updateWorkerFrame():
            frameBtn9 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Items to Change")
            frameBtn9.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colVar = Entry(frameBtn9)
            colVar.insert(END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)
            
            updItmVar = Entry(frameBtn9)
            updItmVar.insert(END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)            
            
            whereItmVar = Entry(frameBtn9)
            whereItmVar.insert(END, "Enter Item ID")
            whereItmVar.place(rely=0.34, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn9, text="Submit", command=lambda: loadUpdateWorkerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn9, text="Close", command=lambda: frameBtn9.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateWorkerField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()                
                updateIndex = whereItmVar.get()                
                ProcessControl.updateWorker(updateColumn, setValue, updateIndex)
                
        button10 = ttk.Button(self.mainFrame, text="Update Job", command=lambda: updateJobFrame())
        button10.place(rely=0.50, relx=0.45)
        
        def updateJobFrame():
            frameBtn10 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Items to Change")
            frameBtn10.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colVar = Entry(frameBtn10)
            colVar.insert(END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)
            
            updItmVar = Entry(frameBtn10)
            updItmVar.insert(END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)            
            
            whereItmVar = Entry(frameBtn10)
            whereItmVar.insert(END, "Enter Item ID")
            whereItmVar.place(rely=0.34, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn10, text="Submit", command=lambda: loadUpdateJobField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn10, text="Close", command=lambda: frameBtn10.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateJobField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()                
                updateIndex = whereItmVar.get()                
                ProcessControl.updateJob(updateColumn, setValue, updateIndex)
                
        button11 = ttk.Button(self.mainFrame, text="Update Comp", command=lambda: updateComputerFrame())
        button11.place(rely=0.70, relx=0.45)
        
        def updateComputerFrame():
            frameBtn11 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Items to Change")
            frameBtn11.place(rely=0.66, relx=0.54, height=200, width=800)
            
            colVar = Entry(frameBtn11)
            colVar.insert(END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)
            
            updItmVar = Entry(frameBtn11)
            updItmVar.insert(END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)            
            
            whereItmVar = Entry(frameBtn11)
            whereItmVar.insert(END, "Enter Item to searched")
            whereItmVar.place(rely=0.34, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn11, text="Submit", command=lambda: loadUpdateComputerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn11, text="Close", command=lambda: frameBtn11.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadUpdateComputerField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()                
                updateIndex = whereItmVar.get()                
                ProcessControl.updateComputer(updateColumn, setValue, updateIndex)
                
        button12 = ttk.Button(self.mainFrame, text="Search Camera", command=lambda: searchCameraFrame())
        button12.place(rely=0.10, relx=0.45)
        
        def searchCameraFrame():
            frameBtn12 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Search Data")
            frameBtn12.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchVar1 = Entry(frameBtn12)
            searchVar1.insert(END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)
            
            searchVar2 = Entry(frameBtn12)
            searchVar2.insert(END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)
            
            writeBtn = ttk.Button(frameBtn12, text="Submit", command=lambda: loadSearchCameraField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn12, text="Close", command=lambda: frameBtn12.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadSearchCameraField():
                read = []
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = ProcessControl.readCamera(searchColumn, searchValue)
                displaySearchCamera(read)
                
            def displaySearchCamera(read):
                tv1.delete(*tv1.get_children())
                for row in read:
                    tv1.insert("", "end", values=row)
            
        button13 = ttk.Button(self.mainFrame, text="Search Worker", command=lambda: searchWorkerFrame())
        button13.place(rely=0.33, relx=0.45)
        
        def searchWorkerFrame():
            frameBtn13 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Search Data")
            frameBtn13.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchVar1 = Entry(frameBtn13)
            searchVar1.insert(END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)
            
            searchVar2 = Entry(frameBtn13)
            searchVar2.insert(END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)
            
            writeBtn = ttk.Button(frameBtn13, text="Submit", command=lambda: loadSearchWorkerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn13, text="Close", command=lambda: frameBtn13.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadSearchWorkerField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = ProcessControl.readWorker(searchColumn, searchValue)
                displaySearchWorker(read)
                
            def displaySearchWorker(read):
                tv2.delete(*tv2.get_children())
                for row in read:
                    tv2.insert("", "end", values=row)
                
        button14 = ttk.Button(self.mainFrame, text="Search Job", command=lambda: searchJobFrame())
        button14.place(rely=0.53, relx=0.45)
        
        def searchJobFrame():
            frameBtn14 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Search Data")
            frameBtn14.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchVar1 = Entry(frameBtn14)
            searchVar1.insert(END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)
            
            searchVar2 = Entry(frameBtn14)
            searchVar2.insert(END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)
            
            writeBtn = ttk.Button(frameBtn14, text="Submit", command=lambda: loadSearchJobField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn14, text="Close", command=lambda: frameBtn14.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadSearchJobField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = ProcessControl.readJob(searchColumn, searchValue)
                displaySearchJob(read)
                
            def displaySearchJob(read):
                tv3.delete(*tv3.get_children())
                for row in read:
                    tv3.insert("", "end", values=row)
                
        button15 = ttk.Button(self.mainFrame, text="Search Comp", command=lambda: searchComputerFrame())
        button15.place(rely=0.73, relx=0.45)
        
        def searchComputerFrame():
            frameBtn15 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Search Data")
            frameBtn15.place(rely=0.66, relx=0.54, height=200, width=800)
            
            searchVar1 = Entry(frameBtn15)
            searchVar1.insert(END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)
            
            searchVar2 = Entry(frameBtn15)
            searchVar2.insert(END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)
            
            writeBtn = ttk.Button(frameBtn15, text="Submit", command=lambda: loadSearchComputerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn15, text="Close", command=lambda: frameBtn15.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadSearchComputerField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = ProcessControl.readComputer(searchColumn, searchValue)
                displaySearchComputer(read)
            
            def displaySearchComputer(read):
                tv4.delete(*tv4.get_children())
                for row in read:
                    tv4.insert("", "end", values=row)             
        
        button16 = ttk.Button(self.mainFrame, text="Delete Camera", command=lambda: delCamFrame())
        button16.place(rely=0.16, relx=0.45)
        
        def delCamFrame():
            frameBtn16 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Item to Delete")
            frameBtn16.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delIdVar = Entry(frameBtn16)
            delIdVar.insert(END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn16, text="Submit", command=lambda: loadCamDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn16, text="Close", command=lambda: frameBtn16.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadCamDeleteField():
                delIdVarg = delIdVar.get()
                delCam = [delIdVarg]
                ProcessControl.deleteCamera(delCam)
                
        button17 = ttk.Button(self.mainFrame, text="Delete Worker", command=lambda: delWorkerFrame())
        button17.place(rely=0.36, relx=0.45)
        
        def delWorkerFrame():
            frameBtn17 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Item to Delete")
            frameBtn17.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delIdVar = Entry(frameBtn17)
            delIdVar.insert(END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn17, text="Submit", command=lambda: loadWorkerDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn17, text="Close", command=lambda: frameBtn17.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadWorkerDeleteField():
                delIdVarg = delIdVar.get()
                delWkr = [delIdVarg]
                ProcessControl.deleteWorker(delWkr)
                
        button18 = ttk.Button(self.mainFrame, text="Delete Job", command=lambda: delJobFrame())
        button18.place(rely=0.56, relx=0.45)
        
        def delJobFrame():
            frameBtn18 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Item to Delete")
            frameBtn18.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delIdVar = Entry(frameBtn18)
            delIdVar.insert(END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)            
            
            writeBtn = ttk.Button(frameBtn18, text="Submit", command=lambda: loadJobDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn18, text="Close", command=lambda: frameBtn18.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadJobDeleteField():
                delIdVarg = delIdVar.get()
                delJob = [delIdVarg]
                ProcessControl.deleteJob(delJob)
                
        button19 = ttk.Button(self.mainFrame, text="Delete Computer", command=lambda: delComputerFrame())
        button19.place(rely=0.76, relx=0.45)
        
        def delComputerFrame():
            frameBtn19 = tk.LabelFrame(self.mainFrame, frameStyles, text="Input Item to Delete")
            frameBtn19.place(rely=0.66, relx=0.54, height=200, width=800)
            
            delIdVar = Entry(frameBtn19)
            delIdVar.insert(END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)
            
            
            writeBtn = ttk.Button(frameBtn19, text="Submit", command=lambda: loadComputerDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn19, text="Close", command=lambda: frameBtn19.destroy())
            closeBtn.place(rely=0.80, relx=0.87)
            
            def loadComputerDeleteField():
                delIdVarg = delIdVar.get()
                delComp = [delIdVarg]
                ProcessControl.deleteComputer(delComp)
                
                        
        tv1 = ttk.Treeview(frame1)
        columnListAccount = ["ID", "Model", "Serial", "Mac Address", "Is Available", "Check Out Date", "Check In Date","Camera Location", "Who Has", "Camera Password", "Price"]
        tv1['columns'] = columnListAccount
        tv1["show"] = "headings"  # removes empty column
        for column in columnListAccount:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame1)
        treeScrollY.configure(command=tv1.yview)
        tv1.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        tv2 = ttk.Treeview(frame3)
        columnListAccount = ["ID", "Name", "Cameras in use", "Items in use"]
        tv2['columns'] = columnListAccount
        tv2["show"] = "headings"  # removes empty column
        for column in columnListAccount:
            tv2.heading(column, text=column)
            tv2.column(column, width=50)
        tv2.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame3)
        treeScrollY.configure(command=tv2.yview)
        tv2.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        tv3 = ttk.Treeview(frame4)
        columnListAccount = ["Job Number", "Company", "Camera Type", "Camera Count", "Camera Serials", "Accessories", "Software Modules", "Purchase Date", "Need by Date", "Job Application", "Testing Status", "Info"]
        tv3['columns'] = columnListAccount
        tv3["show"] = "headings"  # removes empty column
        for column in columnListAccount:
            tv3.heading(column, text=column)
            tv3.column(column, width=50)
        tv3.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame4)
        treeScrollY.configure(command=tv3.yview)
        tv3.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        tv4 = ttk.Treeview(frame5)
        columnListAccount = ["ID", "Processor", "Model", "Service Tag", "RAM", "Price"]
        tv4['columns'] = columnListAccount
        tv4["show"] = "headings"  # removes empty column
        for column in columnListAccount:
            tv4.heading(column, text=column)
            tv4.column(column, width=50)
        tv4.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame5)
        treeScrollY.configure(command=tv4.yview)
        tv4.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")
        
        
        def loadData():
            cameraTable = ProcessControl.viewCameraTable()
            workerTable = ProcessControl.viewWorkerTable()
            jobTable = ProcessControl.viewJobTable()
            computerTable = ProcessControl.viewComputerTable()
            for row in cameraTable:
                tv1.insert("", "end", values=row)
            for row in workerTable:
                tv2.insert("", "end", values=row)
            for row in jobTable:
                tv3.insert("", "end", values=row)
            for row in computerTable:
                tv4.insert("", "end", values=row)
                

        def refreshData():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv4.delete(*tv4.get_children())
            loadData()
            
        
        def clear_data():
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv3.delete(*tv3.get_children())
            
        
        


# class VisualPage(GUI):
#     def __init__(self, parent, controller):
#         GUI.__init__(self, parent)

#         label1 = tk.Label(self.mainFrame, font=("Arial", 20), text="Visual", background="#4b4b4b", foreground="blue")
#         label1.pack(side="top")
        

class AdminPage(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20), text="Admin", background="#4b4b4b", foreground="blue")
        label1.pack(side="top")
        button1 = ttk.Button(self.mainFrame, text="Create Database", command=lambda: ProcessControl.createDatabase(self))
        button1.pack()
        button2 = ttk.Button(self.mainFrame, text="Database Backup", command=lambda: ProcessControl.backupDatabase())
        button2.pack()


# class ReportsPage(GUI):
#     def __init__(self, parent, controller):
#         GUI.__init__(self, parent)

#         label1 = tk.Label(self.mainFrame, font=("Arial", 20), text="Reports Viewer", background="#4b4b4b", foreground="blue")
#         label1.pack(side="top")

#         frame1 = tk.LabelFrame(self, frameStyles, text="Report Left", background="#4b4b4b")
#         frame1.place(rely=0.05, relx=0.02, height=600, width=500)
#         frame2 = tk.LabelFrame(self, frameStyles, text="Report Right")
#         frame2.place(rely=0.05, relx=0.60, height=600, width=500)

#         button1 = tk.Button(self.mainFrame, text="Inventory Report", command=lambda: quit())
#         button1.place(rely=0.05, relx=0.5, height=10, width=25)
#         button1.pack()
#         button2 = tk.Button(self.mainFrame, text="Purchase Orders", command=lambda: quit())
#         button2.place(rely=0.1, relx=0.5, height=10, width=25)
#         button2.pack()

top = LoginPage()
top.title("Cerebrum - Login Page")
root = MyApp()
app=FullScreenApp(root)
root.state('zoomed')
root.withdraw()
root.title("Cerebrum")

root.mainloop()

