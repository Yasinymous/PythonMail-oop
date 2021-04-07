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
        register_screen.geometry("300x600")
    
        global username
        global password
        global mail
        global key
        global username_entry
        global password_entry
        global mail_entry
        global key_entry

        username = StringVar()
        mail = StringVar()
        password = StringVar()
        key = StringVar()
    
        Label(register_screen, text="Please enter details below", bg="blue").pack()
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
        

        key_lable = Label(register_screen, text="Key")
        key_lable.pack()
        key_entry = Entry(register_screen, textvariable=key)
        key_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Confirm", width=10, height=1, bg="blue", command = self.verified_user).pack()
        
    def register_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        global a
        username_control = register.username_control(username_info,db)
        mail_control = register.mail_control(mail_info,db)  
        if(username_control):
            Label(register_screen, text="Username is used", fg="red", font=("calibri", 11)).pack()
        if(mail_control):
            Label(register_screen, text="Mail is used", fg="red", font=("calibri", 11)).pack()
        else:
            a = register.mail_verification(mail)


    def verified_user(self):
        username_info = username.get()
        mail_info = mail.get()
        password_info = password.get()
        key_info = key.get()
        if(register.verified(key_info,a)):
            login_info = User.register(username_info,mail_info,password_info,1,db)   
            if(login_info):
                Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            else:
                Label(register_screen, text="Registration Unsuccess", fg="red", font=("calibri", 11)).pack()
        else:
            Label(register_screen, text="not verified", fg="red", font=("calibri", 11)).pack()


    def login(self):
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
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
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, bg="blue", command = self.login_verify).pack()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        print(username1,password1)
        
        test = register.username_control(username1,db)
        if(test):
            test1 = login.login(username1,password1,db)
            print(test1)
            if(test1):
                self.login_sucess()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()
    
    
    def login_sucess(self):
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
    
    
    def delete_login_success(self):
        login_success_screen.destroy()
    
    
    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()
    
    
    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()
    
    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = self.login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command= self.register).pack()
    
        main_screen.mainloop()
 
