from database.database import Data
from ui.mainscreen import *
import re
import tkinter as tk

db = 'users.db'

data = Data()
data.create_table(db)


