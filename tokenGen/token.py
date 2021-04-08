import random
import datetime

class Token:
    
    def __init__ (self, token, key, date):
        self.key = key
        self.token = token
        self.date = date

    def read(self):
        i = 0
        x = ""
        y = "abcdefghijklmnopqrstuvwxyz0123456789!?_-"
        listem = list(y)
        while(i<31):
            i=i+1
            x += str(random.choice(listem))
        return x

    def token_generate(self):
        return self.read()

    def key_generate(self):
        return self.read()
        
    def date_generate(self):
        return datetime.datetime.now()
        

    def final(self):
        token = self.token_generate()
        key = self.key_generate()
        date = self.date_generate()
        new_token = [token,key,date]
        return new_token