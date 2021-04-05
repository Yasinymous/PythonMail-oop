from database.database import Data

data = Data()

class Register:

    def username_control(self,username,db):
        test = data.UserControl(1,username,db)
        if(test):
            print('var')
        else:
            print('yok')

    def mail_control(self,mail,db):
        test = data.UserControl(3,mail,db)
        if(test):
            print('var')
        else:
            print('yok')

class Login:

    def login(self,username,password,db):
        data.UserLogin(username,password,db)