from mail.sendmail import SendMail
from tokenGen.token import Token
from database.database import Data
from user.user import User

db = 'users.db'

data = Data()
data.create_table(db)

#data.Add_Data1('yasinymous','yasinymous','ysnakyz55@gmail.com',0,db)


#User.register(db)
User.login(db)

#token = Token("","","")
#token.final()

# send = SendMail()
# send.mailgonder()
