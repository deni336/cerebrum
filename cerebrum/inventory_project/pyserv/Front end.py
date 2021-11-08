import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from tkinter import ttk, Menu, font 
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk, Image

from inventory_project.pyserv.Data_process import view_camera_table
#from Data_process import view_camera_table
#from Data_process import *



frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#4b4b4b",
                "fg": "blue", "font": ("Arial", 12, "bold")}


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
        self.show_frame(Welcome_page)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    # def OpenNewWindow(self):
    #     OpenNewWindow()

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

        frame1 = tk.LabelFrame(self, frame_styles, text="Current Inventory Output")
        frame1.place(rely=0.05, relx=0.02, height=600, width=800)
        frame2 = tk.LabelFrame(self, frame_styles, text="Selected Item Display")
        frame2.place(rely=0.05, relx=0.80, height=600, width=200)

        button1 = ttk.Button(self.main_frame, text="Populate from Database", command=lambda: load_data())
        button1.place(rely=0.05, relx=0.5, height=10, width=25)
        button1.pack()
        button2 = ttk.Button(self.main_frame, text="Clear Table", command=lambda: clear_data())
        button2.place(rely=0.1, relx=0.5, height=10, width=25)
        button2.pack()
        button3 = ttk.Button(self.main_frame, text="Refresh Data", command=lambda: refresh_data())
        button3.place(rely=0.15, relx=0.5, height=10, width=25)
        button3.pack()

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["ID", "Type", "Serial", "Mac Address", "Is Available", "Check Out Date", "Check In Date", "Who Has", "Camera Password", "Price"]
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
        
        def load_data():
            camera_table = view_camera_table()
            for row in camera_table:
                tv1.insert("", "end", values=row)

        def refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            load_data()
        
        def clear_data():
            tv1.delete()

        load_data()


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
        button2 = ttk.Button(self.main_frame, text="Purchase Orders", command=lambda: quit())
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

