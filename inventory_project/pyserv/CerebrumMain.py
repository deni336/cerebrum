import threading
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import NO
import CameraViewer as CV
import GUI as G
import InventoryPage as InvPg
import TroubleshootingPage as TP
import AdminPage as AP
import ProcessControl as PC


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
                              command=lambda: parent.showFrame(InvPg.InventoryPage))
        # menu_file.add_command(label="Visual",
        # command=lambda: parent.showFrame(VisualPage))
        # menu_file.add_command(label="Reports",
        # command=lambda: parent.showFrame(ReportsPage))
        menu_file.add_command(label="Admin",
                              command=lambda: parent.showFrame(AP.AdminPage))
        menu_file.add_command(label="Troubleshooting",
                              command=lambda: parent.showFrame(TP.TroubleshootingPage))
        menu_file.add_command(label="Camera Viewer",
                              command=lambda: parent.showFrame(CV.CameraViewer))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)
        help_file.add_command(label="Troubleshooting Guide",
                              command=lambda:
                                  PC.ItemViewProcesses.viewGuide(self))
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
        pages = (InvPg.InventoryPage, AP.AdminPage, TP.TroubleshootingPage, CV.CameraViewer)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(InvPg.InventoryPage)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def quitApplication(self):
        self.destroy()




class OpenNewWindow(G.GUI):

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


top = LoginPage()
top.title("Cerebrum - Login Page")
root = MyApp()
app = FullScreenApp(root)
root.state('zoomed')
root.withdraw()
root.title("Cerebrum")

root.mainloop()
