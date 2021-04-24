import tkinter as Tk
from tkinter import *
import pyodbc as odbc
from pyodbc import *

golfers = Tk()
golfers.title("Golfers")
golfers.geometry('400x600')


# Databases

# Create a Database or Connect to one
conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                    'Database=tgt;'
                    'Trusted_Connection=yes;')
# Create Cursor
c = conn.cursor()



# # #Commit Changes
c.commit()
# Close Connection
c.close()

golfers.mainloop()