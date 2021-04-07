import re

from database.database import Data
from mail.sendmail import SendMail
from tokenGen.token import Token

data = Data()
send = SendMail()

token = Token("","","")

class Register:

    def username_control(self,username,db):
        test = data.UserControl(username,db)
        if(test):
            print('Username is used')
            return True
        return False

    def mail_control(self,mail,db):
        if(self.mail_isvalid(mail)):
            test1 = data.MailControl(mail,db)
            if(test1):
                print('E-mail is used')
                return True
            return False
        return True

    def mail_isvalid(self,mail):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, mail)):
            return True
        else:
            print('wrong char mail')
            return False

    def control(self,username,mail,db):
        test1 = self.username_control(username,db)
        test2 = self.mail_control(mail,db)
        if(test1 or test2):
            return False
        else:
            return True

    def mail_verification(self,mail):
        key = token.final()
        #send.mailgonder(mail,'Verification',key,key)     
        print(key)
        return key
        
    def verified(self,key1,key2):
        if(key1==key2):
            return True
        return False

class Login:

    def login(self,username,password,db):
        return data.UserLogin(username,password,db)

    def user(self,username,db):
        return data.UserInfo(username,db)

    def home(self,db):
        return data.List_Data(db)

    def user_count(self,db):
        return data.usercount(db)