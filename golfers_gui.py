
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

# Create Function to Delete a Record


def delete():
    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=tgt;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()

    # Delete a Record
    c.execute('DELETE from golfers WHERE golfer_id= ' + delete_box.get())

    # Commit Changes
    c.commit()
    # Close Connection
    c.close()

    # Clear boxes
    delete_box.delete(0, END)

# Create Function to Update a Record


def update():  
    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=tgt;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()

    golfer = delete_box.get()

    last = last_name_editor.get()
    first = first_name_editor.get()
    tour = tour_code_editor.get()

    # Update entries
    sql = 'UPDATE golfers SET last_name= ?, first_name=?, tour_code=? WHERE golfer_id=?'
    val = last, first, tour, golfer

    c.execute(sql, val)

    # Commit Changes
    c.commit()
    # Close Connection
    c.close()

# Create a function to edit a record


def edit():
    global editor
    editor = Tk()
    editor.title("Update a Golfer")
    editor.geometry('400x150')

    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=tgt;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the Database
    sql = 'SELECT * from golfers WHERE golfer_id = ?'
    val = record_id
    c.execute(sql, val)
    records = c.fetchall()

    # Create global variables for text box names
    global last_name_editor
    global first_name_editor
    global tour_code_editor

    # Create Text Boxes
    #golfer_id = Entry(golfers, width=30)
    #golfer_id.grid(row=0, column=1, padx=20)
    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=2, column=1, padx=20)
    tour_code_editor = Entry(editor, width=30)
    tour_code_editor.grid(row=3, column=1, padx=20)

    # Create Text Box Labels
    #golfer_id_label = Label(golfers, text="Golfer ID")
    #golfer_id_label.grid(row=0, column=0)
    last_name_label = Label(editor, text="Last Name")
    last_name_label.grid(row=1, column=0, pady=(10, 0))
    first_name_label = Label(editor, text="First Name")
    first_name_label.grid(row=2, column=0)
    tour_code_label = Label(editor, text="Tour Code")
    tour_code_label.grid(row=3, column=0)

    # Loop Through Results
    for record in records:
        last_name_editor.insert(0, record[1])
        first_name_editor.insert(0, record[2])
        tour_code_editor.insert(0, record[3])

    # Create an Save Button
    save_btn = Button(editor, text='Save Record', command=update)
    save_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

    # Update a Record
    sql = 'UPDATE golfers WHERE golfer_id= ?'
    val = delete_box.get()
    c.execute(sql, val)

    # Commit Changes
    c.commit()
    # Close Connection
    c.close()

    # Clear boxes
    editor.destroy()


# Create a function to search
def search():
    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=tgt;'
                        'Trusted_Connection=yes;')
    c = conn.cursor()

    c.execute('SELECT * from golfers ORDER BY last_name DESC')
    records = c.fetchall()


    # print(records)

    # Loop Through Results
    search_results = ''
    for record in records:
        search_results += str(record[0]) + " " + str(record[2]) + \
            " " + str(record[1]) + ": " + str(record[3]) + "\n"

    query_label = Label(golfers, text=search_results)
    query_label.grid(row=7, column=0, columnspan=2)

    # Commit Changes
    c.commit()
    # Close Connection
    c.close()

# Create a function to submt a record
def submit():
    #id = golfer_id.get()
    last = last_name.get()
    first = first_name.get()
    tour = tour_code.get()
    # Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                        'Database=tgt;'
                        'Trusted_Connection=yes;')

    # Create Cursor
    c = conn.cursor()

    # Insert into table
    sql = 'INSERT INTO golfers (last_name, first_name, tour_code) VALUES (?,?,?)'
    val = (last, first, tour)
    c.execute(sql, val)

    # Commit Changes
    c.commit()
    #Message('Records Insterted Successfully...')
    # Close Connection
    c.close()
    # clear the text boxes
    # golfer_id.delete(0,END)
    last_name.delete(0, END)
    first_name.delete(0, END)
    tour_code.delete(0, END)


# Create Text Boxes
golfer_id = Entry(golfers, width=30)
golfer_id.grid(row=0, column=1, padx=20)
last_name = Entry(golfers, width=30)
last_name.grid(row=1, column=1, padx=20, pady=(10, 0))
first_name = Entry(golfers, width=30)
first_name.grid(row=2, column=1, padx=20)
tour_code = Entry(golfers, width=30)
tour_code.grid(row=3, column=1, padx=20)
delete_box = Entry(golfers, width=30)
delete_box.grid(row=9, column=1, )


# Create Text Box Labels
golfer_id_label = Label(golfers, text="Golfer ID")
golfer_id_label.grid(row=0, column=0)
last_name_label = Label(golfers, text="Last Name")
last_name_label.grid(row=1, column=0, pady=(10, 0))
first_name_label = Label(golfers, text="First Name")
first_name_label.grid(row=2, column=0)
tour_code_label = Label(golfers, text="Tour Code")
tour_code_label.grid(row=3, column=0)
delete_box_label = Label(golfers, text="Select ID")
delete_box_label.grid(row=9, column=0)

# Create Submit Button
submit_btn = Button(golfers, text="Add Record", command=submit)
submit_btn.grid(row=4, columnspan=2, pady=10, padx=10, ipadx=139)

# Create a Query Button
qry_btn = Button(golfers, text="Search", command=search)
qry_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a Delete Button
dlt_btn = Button(golfers, text='Delete Selected Record', command=delete)
dlt_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create an Update Button
update_btn = Button(golfers, text='Update Selected Record', command=edit)
update_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

# # #Commit Changes
c.commit()
# Close Connection
c.close()

golfers.mainloop()
