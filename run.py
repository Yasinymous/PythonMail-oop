from database.database import Data
from ui.mainscreen import MainScreen
import re


db = 'users.db'

data = Data()
data.create_table(db)

run = MainScreen()

#data.MailVerified(1,1,db)
run.main_account_screen()

#data.Add_Data1('yasinymous','yasinymous','ysnakyz55@gmail.com',0,db)


#User.register(db)
#User.login(db)


#data.MailUpdate(2,'ysnakyz55@gmail.com',db)
#data.MailDelete('ysnakyz55@gmail.com',db)


#data.List_Data(db)


#token = Token("","","")
#token.final()

# send = SendMail()
# send.mailgonder()
