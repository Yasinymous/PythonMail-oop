from database.database import Data
from .settings import Register, Login

data = Data()
r = Register()
l = Login()


class User:

    def __init__(self, uid, username, password, mail, verified):
        self.uid = uid 
        self.username = username
        self.password = password
        self.mail = mail
        self.verified = verified
    
    def register(db):   
        print('Register')
        username = input('Username : ')
        
        password = input('Password : ')
        mail = input('E-mail : ')
        user_c = r.username_control(username,db)
        mail_c = r.mail_control(mail,db)
        if(user_c == False and mail_c == False):
            print('Username is used')
        else:
            new_user = User(0,username,password,mail,0)
            print ('username {}, password {}, mail {}, verified {}'.format(new_user.username, new_user.password,
                                                                        new_user.mail, new_user.verified))   
            data.Add_Data(new_user,db)
            print('\n')     

    def login(db):
        print('login')
        username = input('Username : ')
        password = input('Password : ')
        l.login(username,password,db)

    def update(self):
        print('update')
    
    def pass_change(self):
        print('pass change')
        
    def mail_verification(self):
        print('mail verification')

        

