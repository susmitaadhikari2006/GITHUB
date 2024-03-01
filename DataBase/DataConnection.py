import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=eccLABS.accdb')
cursor = conn.cursor()
cursor.execute('select * from instructors')
   
for row in cursor.fetchall():
    print(row)