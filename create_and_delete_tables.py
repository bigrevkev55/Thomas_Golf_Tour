
import pyodbc as odbc
from pyodbc import *

def drop_table(table):
    #Create a Database or Connect to one
    conn = odbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                      'Database=tgt;'
                      'Trusted_Connection=yes;')
    c=conn.cursor()
    c.execute(f'DROP TABLE {table}')
    c.commit()
    c.close()
    print(f'{table} has been dropped')

def create_table(table):
  #Create a Database or Connect to one
  conn = odbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                      'Database=tgt;'
                      'Trusted_Connection=yes;')
  #Create Cursor 
  c=conn.cursor()

  c.execute(f"""CREATE TABLE {table}(
      event_id int IDENTITY(1,1) NOT NULL,
      event_name varchar (255),
      purse int
      PRIMARY KEY (event_id))
    """)
  c.commit()
  print(f'{table} has been created')
  c.close

  # c.execute("""CREATE TABLE golfers ( 
  #     golfer_id int IDENTITY(1,1) NOT NULL,
  #     last_name varchar (255),
  # 	first_name varchar (255),
  # 	tour_code varchar(5) FOREIGN KEY REFERENCES tours(tour_code)
  # 	PRIMARY KEY (golfer_id))
  # """)
  print(f"Table '{table}' has been created")

def show_table(table):
    #Create a Database or Connect to one
  conn = odbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-SCL1250\SQLEXPRESS01;'
                      'Database=tgt;'
                      'Trusted_Connection=yes;')
  #Create Cursor 
  c=conn.cursor()
  c.execute(f'SELECT * from {table}')
  records = c.fetchall()
  print(records)


#show_table(table='tours')  #golfers, courses, tours
#create_table(table='courses')
#drop_table(table='test')

