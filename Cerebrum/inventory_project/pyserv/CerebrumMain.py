import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Entry
import ProcessControl as PC

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

database = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventory.db"
databaseBackup = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\inventorybackup.db"
history = r"C:\\Projects\\python_projects\\cerebrum\\Cerebrum\\inventory_project\\history.db"

# for later use


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
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

        mainFrame = tk.Frame(self, bg="#4b4b4b", height=431, width=626)
        mainFrame.pack(fill="both", expand="true")

        self.geometry("626x431")
        self.resizable(0, 0)
        title_styles = {"font": ("Arial", 16),
                        "background": "#4b4b4b", "foreground": "blue"}

        text_styles = {"font": ("Arial", 14),
                       "background": "#4b4b4b",
                       "foreground": "blue"}

        frameLogin = tk.Frame(mainFrame, bg="#4b4b4b", relief="groove", bd=2)
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

        button = ttk.Button(frameLogin, text="Login",
                            command=lambda: getLogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frameLogin, text="Register",
                                command=lambda: getSignup())
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
                tk.messagebox.showerror("Information",
                                        '''The Username or Password you have
                                            entered are incorrect ''')

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
                print('''You need to Register first
                         or amend Line 71 to if True:''')
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

        button = ttk.Button(mainFrame, text="Create Account",
                            command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
            # Creates a text file with the Username and password
            user = entryUser.get()
            pw = entryPw.get()
            validation = validate_user(user)
            if not validation:
                tk.messagebox.showerror("Information",
                                        "That Username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    tk.messagebox.showinfo("Information",
                                           '''Your account details
                                              have been stored.''')
                    SignupPage.destroy(self)

                else:
                    tk.messagebox.showerror("Information",
                                            '''Your password needs to be
                                               longer than 3 values.''')

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
        # menu_file.add_command(label="Welcome",
        # command=lambda: parent.showFrame(WelcomePage))
        menu_file.add_command(label="Inventory Control",
                              command=lambda: parent.showFrame(InventoryPage))
        # menu_file.add_command(label="Visual",
        # command=lambda: parent.showFrame(VisualPage))
        # menu_file.add_command(label="Reports",
        # command=lambda: parent.showFrame(ReportsPage))
        menu_file.add_command(label="Admin",
                              command=lambda: parent.showFrame(AdminPage))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)
        help_file.add_command(label="ReadMe",
                              command=lambda:
                                  PC.ItemViewProcesses.viewReadme(self))


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


class InventoryPage(GUI):

    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Inventory", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, frameStyles,
                               text="Camera Database Output")
        frame1.place(rely=0.05, relx=0.02, height=200, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, frameStyles,
                               text="Selected Item Display")
        frame2.place(rely=0.05, relx=0.85, height=600, width=200)
        frame3 = tk.LabelFrame(self.mainFrame, frameStyles,
                               text="Worker Database Output")
        frame3.place(rely=0.25, relx=0.02, height=200, width=800)
        frame4 = tk.LabelFrame(self.mainFrame, frameStyles,
                               text="Job Database Output")
        frame4.place(rely=0.45, relx=0.02, height=200, width=800)
        frame5 = tk.LabelFrame(self.mainFrame, frameStyles,
                               text="Computer Database Output")
        frame5.place(rely=0.65, relx=0.02, height=200, width=800)

        button2 = ttk.Button(self.mainFrame, text="Clear Table",
                             command=lambda: clear_data())
        button2.place(rely=0.07, relx=0.75)
        button3 = ttk.Button(self.mainFrame, text="Refresh Data",
                             command=lambda: refreshData())
        button3.place(rely=0.07, relx=0.79)

        button4 = ttk.Button(self.mainFrame, text="Add Camera",
                             command=lambda: addCameraFrame())
        button4.place(rely=0.07, relx=0.45)

        def addCameraFrame():

            frameBtn4 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Camera Data")
            frameBtn4.place(rely=0.66, relx=0.54, height=200, width=800)

            modelVar = Entry(frameBtn4)
            modelVar.insert(tk.END, "Camera Model")
            modelVar.place(rely=0.05, relx=0.01)

            serialVar = Entry(frameBtn4)
            serialVar.insert(tk.END, "Serial Number")
            serialVar.place(rely=0.20, relx=0.01)

            macVar = Entry(frameBtn4)
            macVar.insert(tk.END, "MAC Address")
            macVar.place(rely=0.34, relx=0.01)

            availVar = Entry(frameBtn4)
            availVar.insert(tk.END, "Is Camera Available?")
            availVar.place(rely=0.05, relx=0.20)

            dateOutVar = Entry(frameBtn4)
            dateOutVar.insert(tk.END, "Date Checked Out")
            dateOutVar.place(rely=0.48, relx=0.01)

            dateInVar = Entry(frameBtn4)
            dateInVar.insert(tk.END, "Date Checked In")
            dateInVar.place(rely=0.20, relx=0.20)

            cameraLocVar = Entry(frameBtn4)
            cameraLocVar.insert(tk.END, "Camera Location")
            cameraLocVar.place(rely=0.34, relx=0.20)

            whoHasVar = Entry(frameBtn4)
            whoHasVar.insert(tk.END, "Who Has Camera?")
            whoHasVar.place(rely=0.48, relx=0.20)

            cameraPassVar = Entry(frameBtn4)
            cameraPassVar.insert(tk.END, "Camera Password")
            cameraPassVar.place(rely=0.05, relx=0.40)

            priceVar = Entry(frameBtn4)
            priceVar.insert(tk.END, "Price")
            priceVar.place(rely=0.20, relx=0.40)

            idVar = Entry(frameBtn4)
            idVar.insert(tk.END, "Database ID")
            idVar.place(rely=0.34, relx=0.40)

            writeBtn = ttk.Button(frameBtn4, text="Submit",
                                  command=lambda: loadCamCreateField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn4, text="Close",
                                  command=frameBtn4.destroy)
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
                addCam = [idVarg, modelVarg, serialVarg, macVarg, availVarg,
                          dateOutVarg, dateInVarg, cameraLocVarg, whoHasVarg,
                          cameraPassVarg, priceVarg]
                PC.ItemCreationProcesses.createCamera(self, addCam)

        button5 = ttk.Button(self.mainFrame, text="Add Worker",
                             command=lambda: addWorkerFrame())
        button5.place(rely=0.27, relx=0.45)

        def addWorkerFrame():
            frameBtn5 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Worker Data")
            frameBtn5.place(rely=0.66, relx=0.54, height=200, width=800)

            idVar = Entry(frameBtn5)
            idVar.insert(tk.END, "Worker ID")
            idVar.place(rely=0.05, relx=0.01)

            wkrNameVar = Entry(frameBtn5)
            wkrNameVar.insert(tk.END, "Worker Name")
            wkrNameVar.place(rely=0.20, relx=0.01)

            wkrCamVar = Entry(frameBtn5)
            wkrCamVar.insert(tk.END, "Cameras in use")
            wkrCamVar.place(rely=0.34, relx=0.01)

            itmVar = Entry(frameBtn5)
            itmVar.insert(tk.END, "Items in use")
            itmVar.place(rely=0.48, relx=0.01)

            writeBtn = ttk.Button(frameBtn5, text="Submit",
                                  command=lambda: loadWorkerCreateField)
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn5, text="Close",
                                  command=frameBtn5.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadWorkerCreateField():
                idVarg = idVar.get()
                wkrNameVarg = wkrNameVar.get()
                wkrCamVarg = wkrCamVar.get()
                itmVarg = itmVar.get()
                addWorker = [idVarg, wkrNameVarg, wkrCamVarg, itmVarg]
                PC.Processes.createWorker(self, addWorker)

        button6 = ttk.Button(self.mainFrame, text="Add Job",
                             command=lambda: addJobFrame())
        button6.place(rely=0.47, relx=0.45)

        def addJobFrame():
            frameBtn6 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Job Data")
            frameBtn6.place(rely=0.66, relx=0.54, height=200, width=800)

            jobNumVar = Entry(frameBtn6)
            jobNumVar.insert(tk.END, "Job Number")
            jobNumVar.place(rely=0.05, relx=0.01)

            companyVar = Entry(frameBtn6)
            companyVar.insert(tk.END, "Company")
            companyVar.place(rely=0.20, relx=0.01)

            camTypeVar = Entry(frameBtn6)
            camTypeVar.insert(tk.END, "Camera Type")
            camTypeVar.place(rely=0.34, relx=0.01)

            camCountVar = Entry(frameBtn6)
            camCountVar.insert(tk.END, "Camera Count")
            camCountVar.place(rely=0.48, relx=0.01)

            camSerVar = Entry(frameBtn6)
            camSerVar.insert(tk.END, "Camera Serial Numbers")
            camSerVar.place(rely=0.05, relx=0.20)

            accVar = Entry(frameBtn6)
            accVar.insert(tk.END, "Accessories")
            accVar.place(rely=0.20, relx=0.20)

            softModVar = Entry(frameBtn6)
            softModVar.insert(tk.END, "Software Modules")
            softModVar.place(rely=0.34, relx=0.20)

            purDateVar = Entry(frameBtn6)
            purDateVar.insert(tk.END, "Purchase Date")
            purDateVar.place(rely=0.48, relx=0.20)

            arrDateVar = Entry(frameBtn6)
            arrDateVar.insert(tk.END, "Need By Date")
            arrDateVar.place(rely=0.05, relx=0.39)

            itmAppVar = Entry(frameBtn6)
            itmAppVar.insert(tk.END, "Job Application")
            itmAppVar.place(rely=0.20, relx=0.39)

            testStatVar = Entry(frameBtn6)
            testStatVar.insert(tk.END, "Testing Status")
            testStatVar.place(rely=0.34, relx=0.39)

            infoVar = Entry(frameBtn6)
            infoVar.insert(tk.END, "Info")
            infoVar.place(rely=0.48, relx=0.39)

            writeBtn = ttk.Button(frameBtn6, text="Submit",
                                  command=lambda: loadJobCreateField)
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn6, text="Close",
                                  command=frameBtn6.destroy)
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

                addJob = [jobNumVarg, companyVarg, camTypeVarg, camCountVarg,
                          camSerVarg, accVarg, softModVarg, purDateVarg,
                          arrDateVarg, itmAppVarg, testStatVarg, infoVarg]
                PC.ItemCreationProcesses.createJob(self, addJob)

        button7 = ttk.Button(self.mainFrame, text="Add Comp",
                             command=lambda: createComputerFrame())
        button7.place(rely=0.67, relx=0.45)

        def createComputerFrame():
            frameBtn7 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Computer Data")
            frameBtn7.place(rely=0.66, relx=0.54, height=200, width=800)

            idVar = Entry(frameBtn7)
            idVar.insert(tk.END, "Computer ID")
            idVar.place(rely=0.05, relx=0.01)

            procVar = Entry(frameBtn7)
            procVar.insert(tk.END, "Processor")
            procVar.place(rely=0.20, relx=0.01)

            modVar = Entry(frameBtn7)
            modVar.insert(tk.END, "Computer Model")
            modVar.place(rely=0.34, relx=0.01)

            serTagVar = Entry(frameBtn7)
            serTagVar.insert(tk.END, "Service Tag")
            serTagVar.place(rely=0.48, relx=0.01)

            ramVar = Entry(frameBtn7)
            ramVar.insert(tk.END, "RAM")
            ramVar.place(rely=0.05, relx=0.20)

            priceVar = Entry(frameBtn7)
            priceVar.insert(tk.END, "Price")
            priceVar.place(rely=0.20, relx=0.20)

            writeBtn = ttk.Button(frameBtn7, text="Submit",
                                  command=lambda: loadComputerCreateField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn7, text="Close",
                                  command=frameBtn7.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadComputerCreateField():
                idVarg = idVar.get()
                procVarg = procVar.get()
                modVarg = modVar.get()
                serTagVarg = serTagVar.get()
                ramVarg = ramVar.get()
                priceVarg = priceVar.get()
                addComp = [idVarg, procVarg, modVarg, serTagVarg,
                           ramVarg, priceVarg]
                PC.ItemCreationProcesses.createComputer(self, addComp)

        button8 = ttk.Button(self.mainFrame, text="Update Camera",
                             command=lambda: updateCameraFrame())
        button8.place(rely=0.10, relx=0.45)

        def updateCameraFrame():
            frameBtn8 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Items to Change")
            frameBtn8.place(rely=0.66, relx=0.54, height=200, width=800)

            colVar = Entry(frameBtn8)
            colVar.insert(tk.END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)

            updItmVar = Entry(frameBtn8)
            updItmVar.insert(tk.END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)

            whereItmVar = Entry(frameBtn8)
            whereItmVar.insert(tk.END, "Enter Item ID")
            whereItmVar.place(rely=0.34, relx=0.01)

            writeBtn = ttk.Button(frameBtn8, text="Submit",
                                  command=lambda: loadUpdateCameraField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn8, text="Close",
                                  command=frameBtn8.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadUpdateCameraField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()
                updateIndex = whereItmVar.get()
                PC.ItemUpdateProcesses.updateCamera(self, updateColumn,
                                                    setValue, updateIndex)

        button9 = ttk.Button(self.mainFrame, text="Update Worker",
                             command=lambda: updateWorkerFrame())
        button9.place(rely=0.30, relx=0.45)

        def updateWorkerFrame():
            frameBtn9 = tk.LabelFrame(self.mainFrame, frameStyles,
                                      text="Input Items to Change")
            frameBtn9.place(rely=0.66, relx=0.54, height=200, width=800)

            colVar = Entry(frameBtn9)
            colVar.insert(tk.END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)

            updItmVar = Entry(frameBtn9)
            updItmVar.insert(tk.END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)

            whereItmVar = Entry(frameBtn9)
            whereItmVar.insert(tk.END, "Enter Item ID")
            whereItmVar.place(rely=0.34, relx=0.01)

            writeBtn = ttk.Button(frameBtn9, text="Submit",
                                  command=lambda: loadUpdateWorkerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn9, text="Close",
                                  command=frameBtn9.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadUpdateWorkerField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()
                updateIndex = whereItmVar.get()
                PC.ItemUpdateProcesses.updateWorker(self, updateColumn,
                                                    setValue, updateIndex)

        button10 = ttk.Button(self.mainFrame, text="Update Job",
                              command=lambda: updateJobFrame())
        button10.place(rely=0.50, relx=0.45)

        def updateJobFrame():
            frameBtn10 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Items to Change")
            frameBtn10.place(rely=0.66, relx=0.54, height=200, width=800)

            colVar = Entry(frameBtn10)
            colVar.insert(tk.END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)

            updItmVar = Entry(frameBtn10)
            updItmVar.insert(tk.END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)

            whereItmVar = Entry(frameBtn10)
            whereItmVar.insert(tk.END, "Enter Item ID")
            whereItmVar.place(rely=0.34, relx=0.01)

            writeBtn = ttk.Button(frameBtn10, text="Submit",
                                  command=lambda: loadUpdateJobField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn10, text="Close",
                                  command=frameBtn10.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadUpdateJobField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()
                updateIndex = whereItmVar.get()
                PC.ItemUpdateProcesses.updateJob(self, updateColumn,
                                                 setValue, updateIndex)

        button11 = ttk.Button(self.mainFrame, text="Update Comp",
                              command=lambda: updateComputerFrame())
        button11.place(rely=0.70, relx=0.45)

        def updateComputerFrame():
            frameBtn11 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Items to Change")
            frameBtn11.place(rely=0.66, relx=0.54, height=200, width=800)

            colVar = Entry(frameBtn11)
            colVar.insert(tk.END, "Column to Change")
            colVar.place(rely=0.05, relx=0.01)

            updItmVar = Entry(frameBtn11)
            updItmVar.insert(tk.END, "New Data")
            updItmVar.place(rely=0.20, relx=0.01)

            whereItmVar = Entry(frameBtn11)
            whereItmVar.insert(tk.END, "Enter Item to searched")
            whereItmVar.place(rely=0.34, relx=0.01)

            writeBtn = ttk.Button(frameBtn11, text="Submit",
                                  command=lambda: loadUpdateComputerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn11, text="Close",
                                  command=frameBtn11.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadUpdateComputerField():
                updateColumn = colVar.get()
                setValue = updItmVar.get()
                updateIndex = whereItmVar.get()
                PC.ItemUpdateProcesses.updateComputer(self, updateColumn,
                                                      setValue, updateIndex)

        button12 = ttk.Button(self.mainFrame, text="Search Camera",
                              command=lambda: searchCameraFrame())
        button12.place(rely=0.13, relx=0.45)

        def searchCameraFrame():
            frameBtn12 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Search Data")
            frameBtn12.place(rely=0.66, relx=0.54, height=200, width=800)

            searchVar1 = Entry(frameBtn12)
            searchVar1.insert(tk.END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)

            searchVar2 = Entry(frameBtn12)
            searchVar2.insert(tk.END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)

            writeBtn = ttk.Button(frameBtn12, text="Submit",
                                  command=lambda: loadSearchCameraField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn12, text="Close",
                                  command=frameBtn12.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadSearchCameraField():
                read = []
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = PC.ItemReadProcesses.readCamera(self, searchColumn,
                                                       searchValue)
                displaySearchCamera(read)

            def displaySearchCamera(read):
                tv1.delete(*tv1.get_children())
                for row in read:
                    tv1.insert("", "end", values=row)

        button13 = ttk.Button(self.mainFrame, text="Search Worker",
                              command=lambda: searchWorkerFrame())
        button13.place(rely=0.33, relx=0.45)

        def searchWorkerFrame():
            frameBtn13 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Search Data")
            frameBtn13.place(rely=0.66, relx=0.54, height=200, width=800)

            searchVar1 = Entry(frameBtn13)
            searchVar1.insert(tk.END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)

            searchVar2 = Entry(frameBtn13)
            searchVar2.insert(tk.END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)

            writeBtn = ttk.Button(frameBtn13, text="Submit",
                                  command=lambda: loadSearchWorkerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn13, text="Close",
                                  command=frameBtn13.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadSearchWorkerField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = PC.ItemReadProcesses.readWorker(self, searchColumn,
                                                       searchValue)
                displaySearchWorker(read)

            def displaySearchWorker(read):
                tv2.delete(*tv2.get_children())
                for row in read:
                    tv2.insert("", "end", values=row)

        button14 = ttk.Button(self.mainFrame, text="Search Job",
                              command=lambda: searchJobFrame())
        button14.place(rely=0.53, relx=0.45)

        def searchJobFrame():
            frameBtn14 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Search Data")
            frameBtn14.place(rely=0.66, relx=0.54, height=200, width=800)

            searchVar1 = Entry(frameBtn14)
            searchVar1.insert(tk.END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)

            searchVar2 = Entry(frameBtn14)
            searchVar2.insert(tk.END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)

            writeBtn = ttk.Button(frameBtn14, text="Submit",
                                  command=lambda: loadSearchJobField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn14, text="Close",
                                  command=frameBtn14.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadSearchJobField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = PC.ItemReadProcesses.readJob(self, searchColumn,
                                                    searchValue)
                displaySearchJob(read)

            def displaySearchJob(read):
                tv3.delete(*tv3.get_children())
                for row in read:
                    tv3.insert("", "end", values=row)

        button15 = ttk.Button(self.mainFrame, text="Search Comp",
                              command=lambda: searchComputerFrame())
        button15.place(rely=0.73, relx=0.45)

        def searchComputerFrame():
            frameBtn15 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Search Data")
            frameBtn15.place(rely=0.66, relx=0.54, height=200, width=800)

            searchVar1 = Entry(frameBtn15)
            searchVar1.insert(tk.END, "Enter Column to Search by")
            searchVar1.place(rely=0.05, relx=0.01)

            searchVar2 = Entry(frameBtn15)
            searchVar2.insert(tk.END, "Enter Search Value")
            searchVar2.place(rely=0.20, relx=0.01)

            writeBtn = ttk.Button(frameBtn15, text="Submit",
                                  command=lambda: loadSearchComputerField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn15, text="Close",
                                  command=frameBtn15.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadSearchComputerField():
                searchColumn = searchVar1.get()
                searchValue = searchVar2.get()
                read = PC.ItemReadProcesses.readComputer(self, searchColumn,
                                                         searchValue)
                displaySearchComputer(read)

            def displaySearchComputer(read):
                tv4.delete(*tv4.get_children())
                for row in read:
                    tv4.insert("", "end", values=row)

        button16 = ttk.Button(self.mainFrame, text="Delete Camera",
                              command=lambda: delCamFrame())
        button16.place(rely=0.16, relx=0.45)

        def delCamFrame():
            frameBtn16 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Item to Delete")
            frameBtn16.place(rely=0.66, relx=0.54, height=200, width=800)

            delIdVar = Entry(frameBtn16)
            delIdVar.insert(tk.END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)

            writeBtn = ttk.Button(frameBtn16, text="Submit",
                                  command=lambda: loadCamDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn16, text="Close",
                                  command=frameBtn16.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadCamDeleteField():
                delIdVarg = delIdVar.get()
                delCam = [delIdVarg]
                PC.ItemDeleteProcesses.deleteCamera(self, delCam)

        button17 = ttk.Button(self.mainFrame, text="Delete Worker",
                              command=lambda: delWorkerFrame())
        button17.place(rely=0.36, relx=0.45)

        def delWorkerFrame():
            frameBtn17 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Item to Delete")
            frameBtn17.place(rely=0.66, relx=0.54, height=200, width=800)

            delIdVar = Entry(frameBtn17)
            delIdVar.insert(tk.END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)

            writeBtn = ttk.Button(frameBtn17, text="Submit",
                                  command=lambda: loadWorkerDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn17, text="Close",
                                  command=frameBtn17.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadWorkerDeleteField():
                delIdVarg = delIdVar.get()
                delWkr = [delIdVarg]
                PC.ItemDeleteProcesses.deleteWorker(self, delWkr)

        button18 = ttk.Button(self.mainFrame, text="Delete Job",
                              command=lambda: delJobFrame())
        button18.place(rely=0.56, relx=0.45)

        def delJobFrame():
            frameBtn18 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Item to Delete")
            frameBtn18.place(rely=0.66, relx=0.54, height=200, width=800)

            delIdVar = Entry(frameBtn18)
            delIdVar.insert(tk.END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)

            writeBtn = ttk.Button(frameBtn18, text="Submit",
                                  command=lambda: loadJobDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn18, text="Close",
                                  command=frameBtn18.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadJobDeleteField():
                delIdVarg = delIdVar.get()
                delJob = [delIdVarg]
                PC.ItemDeleteProcesses.deleteJob(self, delJob)

        button19 = ttk.Button(self.mainFrame, text="Delete Computer",
                              command=lambda: delComputerFrame())
        button19.place(rely=0.76, relx=0.45)

        def delComputerFrame():
            frameBtn19 = tk.LabelFrame(self.mainFrame, frameStyles,
                                       text="Input Item to Delete")
            frameBtn19.place(rely=0.66, relx=0.54, height=200, width=800)

            delIdVar = Entry(frameBtn19)
            delIdVar.insert(tk.END, "Enter ID to be Deleted")
            delIdVar.place(rely=0.05, relx=0.01)

            writeBtn = ttk.Button(frameBtn19, text="Submit",
                                  command=lambda: loadComputerDeleteField())
            writeBtn.place(rely=0.80, relx=0.77)
            closeBtn = ttk.Button(frameBtn19, text="Close",
                                  command=frameBtn19.destroy)
            closeBtn.place(rely=0.80, relx=0.87)

            def loadComputerDeleteField():
                delIdVarg = delIdVar.get()
                delComp = [delIdVarg]
                PC.ItemDeleteProcesses.deleteComputer(self, delComp)

        tv1 = ttk.Treeview(frame1)
        columnListAccount = ["ID", "Model", "Serial", "Mac Address",
                             "Is Available", "Check Out Date", "Check In Date",
                             "Camera Location", "Who Has", "Camera Password",
                             "Price"]
        tv1['columns'] = columnListAccount
        tv1["show"] = "headings"
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
        tv2["show"] = "headings"
        for column in columnListAccount:
            tv2.heading(column, text=column)
            tv2.column(column, width=50)
        tv2.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame3)
        treeScrollY.configure(command=tv2.yview)
        tv2.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        tv3 = ttk.Treeview(frame4)
        columnListAccount = ["Job Number", "Company", "Camera Type",
                             "Camera Count", "Camera Serials", "Accessories",
                             "Software Modules", "Purchase Date",
                             "Need by Date", "Job Application",
                             "Testing Status", "Info"]
        tv3['columns'] = columnListAccount
        tv3["show"] = "headings"
        for column in columnListAccount:
            tv3.heading(column, text=column)
            tv3.column(column, width=50)
        tv3.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame4)
        treeScrollY.configure(command=tv3.yview)
        tv3.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        tv4 = ttk.Treeview(frame5)
        columnListAccount = ["ID", "Processor", "Model", "Service Tag",
                             "RAM", "Price"]
        tv4['columns'] = columnListAccount
        tv4["show"] = "headings"
        for column in columnListAccount:
            tv4.heading(column, text=column)
            tv4.column(column, width=50)
        tv4.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame5)
        treeScrollY.configure(command=tv4.yview)
        tv4.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        def loadData():
            cameraTable = PC.ItemViewProcesses.viewCameraTable(self, database)
            workerTable = PC.ItemViewProcesses.viewWorkerTable(self, database)
            jobTable = PC.ItemViewProcesses.viewJobTable(self, database)
            computerTable = PC.ItemViewProcesses.viewComputerTable(self, database)
            for row in cameraTable:
                tv1.insert("", "end", values=row)
            for row in workerTable:
                tv2.insert("", "end", values=row)
            for row in jobTable:
                tv3.insert("", "end", values=row)
            for row in computerTable:
                tv4.insert("", "end", values=row)


        def refreshData():
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv4.delete(*tv4.get_children())
            loadData()

        def clear_data():
            tv1.delete(*tv1.get_children())
            tv2.delete(*tv2.get_children())
            tv3.delete(*tv3.get_children())
            tv4.delete(*tv4.get_children())

        loadData()


class AdminPage(GUI):
    def __init__(self, parent, controller):

        GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Admin", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")
        frame1 = tk.LabelFrame(self, frameStyles,
                               text="Historical Changes", background="#4b4b4b")
        frame1.place(rely=0.05, relx=0.02, height=600, width=500)
        button1 = ttk.Button(self.mainFrame,
                             text="Create Database", command=lambda:
                             PC.DatabaseCreationProcesses.createDatabase(self))
        button1.pack()
        button2 = ttk.Button(self.mainFrame,
                             text="Database Backup", command=lambda:
                             PC.DatabaseCreationProcesses.backupDatabase(self))
        button2.pack()
        button2 = ttk.Button(self.mainFrame,
                             text="Restore Database", command=lambda:
                             PC.DatabaseCreationProcesses.restoreFromBackup(self))
        button2.pack()
        
        tv5 = ttk.Treeview(frame1)
        columnListAccount = ["", "", "", "", "", "", "", "", "", "", ""]
        tv5['columns'] = columnListAccount
        tv5["show"] = "headings" 
        for column in columnListAccount:
            tv5.heading(column, text=column)
            tv5.column(column, width=50)
        tv5.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame1)
        treeScrollY.configure(command=tv5.yview)
        tv5.configure(yscrollcomman=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")

        def populate(self):
            cameraTable = PC.ItemViewProcesses.viewCameraTable(self, history)
            workerTable = PC.ItemViewProcesses.viewWorkerTable(self, history)
            jobTable = PC.ItemViewProcesses.viewJobTable(self, history)
            computerTable = PC.ItemViewProcesses.viewComputerTable(self, history)
            for row in cameraTable:
                tv5.insert("", "end", values=row)
            for row in workerTable:
                tv5.insert("", "end", values=row)
            for row in jobTable:
                tv5.insert("", "end", values=row)
            for row in computerTable:
                tv5.insert("", "end", values=row)
        populate(self)


top = LoginPage()
top.title("Cerebrum - Login Page")
root = MyApp()
app = FullScreenApp(root)
root.state('zoomed')
root.withdraw()
root.title("Cerebrum")

root.mainloop()
