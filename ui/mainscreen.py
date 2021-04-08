import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

import time 
from threading import Thread
from user.user import User
from database.database import Data
from user.settings import Register, Login

db = 'users.db'

data = Data()
register = Register()
login = Login()

LARGEFONT =("Verdana", 20)
NORMALFONT =("Verdana", 15)


  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self,bg="blue") 
        container.pack(side = "top", expand = True, fill = "both")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text ="Home", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.place(x=20, y=40)
        
        button1 = ttk.Button(self, text ="Login", 
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.place(x=165, y=5)
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Register",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.place(x=255, y=5)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        # button to show frame 2 with text
        # layout2

        button1 = ttk.Button(self, text ="Login",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place
        # by using grid
        button1.place(x=165, y=5)
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Register",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.place(x=255, y=5)

        ## LOGİN INPUT   
        label = ttk.Label(self, text ="Login", font = LARGEFONT)
        label.place(x=20, y=40)
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
        
        global username_login_entry
        global password_login_entry
    
        label = ttk.Label(self, text ="Username", font = NORMALFONT)
        label.place(x=20, y=80)
        username_login_entry = Entry(self, textvariable=username_verify)
        username_login_entry.place(x=20, y=100)
  

        label = ttk.Label(self, text ="Password", font = NORMALFONT)
        label.place(x=20, y=130)
        password_login_entry = Entry(self, textvariable=password_verify, show= '*')
        password_login_entry.place(x=20, y=150)

        button3 = ttk.Button(self, text ="Login",
                            command = self.login_verify)
        button3.place(x=20, y=180)
    
    def login_verify(self):
        global username1
        username1 = username_verify.get()
        password1 = password_verify.get()
        print(username1,password1)
        
        test = register.username_control(username1,db)
        if(test):
            test1 = login.login(username1,password1,db)
            print(test1)
            if(test1):
                self.popup_loginsuccess()
                self.profile(username1)
            else:
                self.popup_passwordwrong()
        else:
            self.popup_usernotfound()

    
    def popup_usernotfound(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="User Not Found")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_loginsuccess(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Login Succes")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_passwordwrong(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Password Wrong")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()



# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Register", font = LARGEFONT)
        label.place(x=20, y=40)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Login",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.place(x=165, y=5)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Register",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.place(x=255, y=5)

        global username
        global password
        global mail
        global username_entry
        global password_entry
        global mail_entry

        username = StringVar()
        mail = StringVar()
        password = StringVar()

        label = ttk.Label(self, text ="Username", font = NORMALFONT)
        label.place(x=20, y=80)
        username_entry = Entry(self, textvariable=username)
        username_entry.place(x=20, y=100)
  
        label = ttk.Label(self, text ="E-mail", font = NORMALFONT)
        label.place(x=20, y=130)
        mail_entry = Entry(self, textvariable=mail)
        mail_entry.place(x=20, y=150)

        label = ttk.Label(self, text ="Password", font = NORMALFONT)
        label.place(x=20, y=180)
        password_entry = Entry(self, textvariable=password, show= '*')
        password_entry.place(x=20, y=200)
        
        button3 = ttk.Button(self, text ="Register",
                            command = self.register_user)
        button3.place(x=20, y=230)

    def register_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        global a
        if(username_info == "" or mail_info == "" or password_info == ""):
            print("bosluk")
            #self.null()
        else:
            username_control = register.username_control(username_info,db)
            mail_control = register.mail_control(mail_info,db)  

            if(username_control):
                self.popup_usernameused()
            if(mail_control):
                self.popup_mailused()
            if(mail_control == False and username_control == False and password_info !=""):
                self.popup_mailsend(mail_info)   
                a = register.mail_verification(mail_info)
                app.show_frame(Page3)

    def popup_usernameused(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Username is used.")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_mailused(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="E-Mail is used.")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_mailsend(self,mail_info):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text=mail_info+",Mail send.")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_null(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Fill in the blanks.")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()

class Page3(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Verification", font = LARGEFONT)
        label.place(x=20, y=40)

        global key
        global key_entry

        key = StringVar()

        label = ttk.Label(self, text ="Key", font = NORMALFONT)
        label.place(x=20, y=80)
        key_entry = Entry(self, textvariable=key)
        key_entry.place(x=20, y=100)

        button1 = ttk.Button(self, text ="Confirm",
                            command = self.verified_user)
        button1.place(x=20, y=130)


    def verified_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        key_info = key.get()
        if(register.verified(key_info,a[1])):
            login_info = User.register(username_info,mail_info,password_info,1,db)   
            if(login_info):
                self.popup_success()
                app.show_frame(Page1)
                app.update()
            else:
                self.popup_unsuccess()
                app.update()
        else:
            self.popup_unverified()
    
    def popup_success(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Registration Successful")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_unsuccess(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Registration Unsuccessful!")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()
    def popup_unverified(self):
        win = tk.Toplevel()
        win.wm_title("Info")
        win.geometry("200x100")
        win.resizable(0,0)
        l = tk.Label(win, text="Verified Unsuccessful")
        l.pack()
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.pack()


  
app = tkinterApp()
app.geometry("350x350")
app.resizable(0,0)
app.mainloop()


