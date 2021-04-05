import sqlite3


class Data:

    def connect(self,db):
        self.connection = sqlite3.connect(db)
        return self.connection

    def con_commit_close(self,connection):
        connection.commit()
        connection.close()

    def create_table(self,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Users(uid INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(64) UNIQUE, password VARCHAR(256), mail TEXT, verified INT)')
        self.con_commit_close(connection)

    def Control_Data_UID(self,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            new_uid = uid[0]+1
        return new_uid
             
    def Add_Data(self,data,db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users(username, password, mail, verified) VALUES (?,?,?,?)',(data.username,data.password,data.mail,data.verified))
        self.con_commit_close(connection)

    def Add_Data1(self,username,password,mail,verified,db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users(username, password, mail, verified) VALUES (?,?,?,?)',(username,password,mail,verified))
        self.con_commit_close(connection)
    
    def Delete_Data(self,uid,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Users WHERE uid=?',(uid,))
        self.con_commit_close(connection)

    def List_Data(self,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            print(uid)    
           

    def Search_Data(self,search_id,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        new_uid = 0
        for uid in cursor.fetchall():
            if (search_id == uid[0]):
                return True
            else:
                return False

    def UserControl(self,index,control,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users')
        for user in cursor.fetchall():
            if (control == user[index]):
                return True
            else:
                return False

    def UserLogin(self,username,password,db):
        connection = self.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT * from Users WHERE username="%s" AND password="%s"' % (username, password))
        if cursor.fetchone() is not None:
            print("Welcome")
        else:
            print("Login failed")