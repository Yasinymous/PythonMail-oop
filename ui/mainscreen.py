from tkinter import *

from user.user import User
from database.database import Data
from user.settings import Register, Login

db = 'users.db'

data = Data()
register = Register()
login = Login()

class MainScreen:
    
    def register(self):
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("350x350")
    
        global username
        global password
        global mail
        global username_entry
        global password_entry
        global mail_entry

        username = StringVar()
        mail = StringVar()
        password = StringVar()

        Label(register_screen, text="Register", width="300", height="2", font=("Calibri", 20)).pack()
        Label(register_screen, text="").pack()
        
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()

        mail_lable = Label(register_screen, text="E-mail * ")
        mail_lable.pack()
        mail_entry = Entry(register_screen, textvariable=mail)
        mail_entry.pack()
        
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command = self.register_user).pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Back Page", width=10, height=1, bg="blue", command = self.RegistertoMain).pack()
        

    def register_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        global a

        if(username_info == "" or mail_info == "" or password_info == ""):
            self.null()
        else:
            username_control = register.username_control(username_info,db)
            mail_control = register.mail_control(mail_info,db)  
            if(username_control):
                self.username_used()
            if(mail_control):
                self.mail_used()
            if(mail_control == False and username_control == False and password_info !=""):
                a = register.mail_verification(mail)
                self.key_verify()
            

    def key_verify(self):
        global key_screen
        key_screen = Toplevel(register_screen)
        key_screen.title("key ")
        key_screen.geometry("300x150")

        global key
        global key_entry

        key = StringVar()

        key_lable = Label(key_screen, text="Key")
        key_lable.pack()
        key_entry = Entry(key_screen, textvariable=key)
        key_entry.pack()

        Label(key_screen, text="").pack()
        Button(key_screen, text="Confirm", width=10, height=1, bg="blue", command = self.verified_user).pack()

    def verified_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        key_info = key.get()
        if(register.verified(key_info,a)):
            login_info = User.register(username_info,mail_info,password_info,1,db)   
            if(login_info):
                self.verified_success()
            else:
                self.verified_test(0)
        else:
            self.verified_test(1)
  
    def verified_success(self):
        global verified_screen_success
        verified_screen_success = Toplevel(key_screen)
        verified_screen_success.geometry("150x100")
        verified_screen_success.title("Success")
        Label(verified_screen_success, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        Button(verified_screen_success, text="OK", command=self.off_verified_success).pack()

    def off_verified_success(self):
        verified_screen_success.destroy()
        key_screen.destroy()
        register_screen.destroy()

    def verified_test(self,num):
        global verified_screen
        verified_screen = Toplevel(key_screen)
        verified_screen.geometry("150x100")
        if(num==0):
            verified_screen.title("Unsuccess")
            Label(verified_screen, text="Registration Unsuccess", fg="red", font=("calibri", 11)).pack()
            Button(verified_screen, text="OK", command=self.off_verified_screen).pack()
        else:
            verified_screen.title("Wrong key")
            Label(verified_screen, text="un verified", fg="red", font=("calibri", 11)).pack()
            Button(verified_screen_screen, text="OK", command=self.exit_verified_screen).pack()

    def login(self):
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("350x350")
        Label(login_screen, text="Login", width="300", height="2", font=("Calibri", 20)).pack()
        Label(login_screen, text="").pack()
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_login_entry
        global password_login_entry
    
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, bg="blue", command = self.login_verify).pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Back Page", width=10, height=1, bg="blue", command = self.LogintoMain).pack()


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
                self.login_success()
                self.profile(username1)
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()
    def run():
    #window config
        window = tkinter.Toplevel()
            
    def profile(self,username):
        global profile_screen
        profile_screen = Toplevel(login_screen)
        profile_screen.title("Profile")
        profile_screen.geometry("300x300")

        user_info = login.user(username,db)
        Label(profile_screen, text=user_info[1]).pack()
        Label(profile_screen, text=user_info[2]).pack()
        Label(profile_screen, text=user_info[3]).pack()
        Button(profile_screen, text="home", command=self.home).pack()
        Button(profile_screen, text="Exit", command=self.profile_exit).pack()

    def home(self):
        global home_screen
        home_screen = Toplevel(profile_screen)
        home_screen.title("Profile")
        home_screen.geometry("500x300")
        home_info = login.home(db)
        user_count = login.user_count(db)
        label = Label(home_screen, text = "username - e-mail") 
        Lb1 = Listbox(home_screen,width=35)
        i = 0 
        for home in home_info.fetchall():
            Lb1.insert(i,"-"+home[1]+","+home[3])
            i+=1  
        label.pack()
        Lb1.pack()
        Button(home_screen, text="Profile", command=self.homeback).pack()
        Button(home_screen, text="Exit", command=self.homeexit).pack()

    def username_used(self):
        global username_used_screen
        username_used_screen = Toplevel(register_screen)
        username_used_screen.title("Username Is Used")
        username_used_screen.geometry("150x100")
        Label(username_used_screen, text="Username is used").pack()
        Button(username_used_screen, text="OK", command=self.usernameusedexit).pack()

    def mail_used(self):
        global mail_used_screen
        mail_used_screen = Toplevel(register_screen)
        mail_used_screen.title("Email Is Used")
        mail_used_screen.geometry("150x100")
        Label(mail_used_screen, text="E-mail is used").pack()
        Button(mail_used_screen, text="OK", command=self.mailusedexit).pack()

    def null(self):
        global null_screen
        null_screen = Toplevel(register_screen)
        null_screen.title("Null")
        null_screen.geometry("150x100")
        Label(null_screen, text="Null").pack()
        Button(null_screen, text="OK", command=self.null_exit).pack()

    def login_success(self):
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=self.delete_login_success).pack()

    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()
    
    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()
    
    def usernameusedexit(self):
        username_used_screen.destroy()

    def mailusedexit(self):
        mail_used_screen.destroy()

    def null_exit(self):
        null_screen.destroy()

    def main_exit(self):
        main_screen.destroy()
    
    def delete_login_success(self):
        login_success_screen.destroy()  
    
    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()
    
    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()
    
    def homeback(self):
        home_screen.destroy()

    def homeexit(self):
        home_screen.destroy()
        self.profile_exit()

    def profile_exit(self):
        profile_screen.destroy()
        login_screen.destroy()

    def exit_verified_screen(self):
        verified_screen.destroy()

    def RegistertoMain(self):
        register_screen.destroy()

    def LogintoMain(self):
        login_screen.destroy()


    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("350x350")
        main_screen.title("Account Login")
        Label(text="Login Register", width="300", height="2", font=("Calibri", 20)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = self.login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command= self.register).pack()

    
        main_screen.mainloop()
    
