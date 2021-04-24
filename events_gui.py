import tkinter as Tk
from tkinter import *
import pyodbc as odbc
from pyodbc import *

events = Tk()
events.title("Events")
events.geometry('400x600')


# Databases

# Create a Database or Connect to one
conn = odbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                    'Database=tgt;'
                    'Trusted_Connection=yes;')
# Create Cursor
c = conn.cursor()

# Create Functions

# Create Text Boxes
event_id = Entry(events, width=30)
event_id.grid(row=1, column=1, padx=20)
event_type = Entry(events, width=30)
event_type.grid(row=2, column=1, padx=20)
event_name = Entry(events, width=30)
event_name.grid(row=3, column=1, padx=20)
event_winner = Entry(events, width=30)
event_winner.grid(row=4, column=1, padx=20)
purse = Entry(events, width=30)
purse.grid(row=5, column=1, padx=20)
_first = Entry(events, width=30)
_first.grid(row=6, column=1, padx=20)
_second = Entry(events, width=30)
_second.grid(row=7, column=1, padx=20)
_third = Entry(events, width=30)
_third.grid(row=8, column=1, padx=20)
_fourth_to_tenth = Entry(events, width=30)
_fourth_to_tenth.grid(row=9, column=1, padx=20)


# Create Text Box Labels
event_id_label = Label(events, text="Event ID")
event_id_label.grid(row=1, column=0, padx=20)
event_type_label = Label(events, text="Event Type")
event_type_label.grid(row=2, column=0, padx=20)
event_name_label = Label(events, text="Event Name")
event_name_label.grid(row=3, column=0, padx=20)
event_winner_label = Label(events, text="Event Winner")
event_winner_label.grid(row=4, column=0, padx=20)
purse_label = Label(events, text="Purse")
purse_label.grid(row=5, column=0, padx=20)
_first_label = Label(events, text="Winner $")
_first_label.grid(row=6, column = 0, padx=20)
_second_label = Label(events, text="Second $")
_second_label.grid(row=7, column = 0, padx=20)
_third_label = Label(events, text='Third $')
_third_label.grid(row=8, column=0, padx=20)
_fourth_to_tenth_label = Label(events, text='Fourth to Tenth $')
_fourth_to_tenth_label.grid(row=9, column=0, padx=20)

# Create Buttons



# # #Commit Changes
c.commit()
# Close Connection
c.close()

events.mainloop()