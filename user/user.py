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
    
    def register(username,mail,password,verified,db):   
        print('Register')
        test = r.control(username,mail,db)
        if(test):
            new_user = User(0,username,password,mail,verified)
            print ('username {}, password {}, mail {}, verified {}'.format(new_user.username, new_user.password,
                                                                        new_user.mail, new_user.verified))   
            data.Add_Data(new_user,db)
            print('\n')     
            return True
        return False

    def login(db):
        print('login')
        username = input('Username : ')
        password = input('Password : ')
        l.login(username,password,db)

    def update(self):
        print('update')
    
    def pass_change(self):
        print('pass change')
        

