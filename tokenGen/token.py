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
        y = "abcdefghijklmnopqrstuvwxyz0123456789!?_-*."
        listem = list(y)
        while(i<31):
            i=i+1
            x += str(random.choice(listem))
        print(x)
        return x

    def token_generate(self):
        self.read()

    def key_generate(self):
        self.read()
        
    def date_generate(self):
        an = datetime.datetime.now()
        print(an)

    def final(self):
        self.token_generate()
        self.key_generate()
        self.date_generate()