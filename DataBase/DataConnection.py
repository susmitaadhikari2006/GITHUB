import pyodbc

driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
filePath = r'C:\Users\PS24Sadhikari\python\GITHUB\DataBase\ECCLabs.accdb'
myDataSource = pyodbc.dataSources()
access_driver = myDataSource['MS Access Database']

conn = pyodbc.connect(driver = access_driver, dbq = filePath, autocommit=True)

cursor = conn.cursor()
cursor.execute('select * from tblLabPrograms')

n=1
print("\n Labs Information: \n")
for row in cursor.fetchall():
    print(str(n) + ". " + str(row))
    n+=1
    cursor = conn.cursor()

print("\n Instructor Information: \n")
cursor.execute('select firstName, lastName, Email  from tbl_instructors')
   
for row in cursor.fetchall():
    print(row)

print("\n query Information: \n")

cursor.execute('SELECT tblLabPrograms.Abbrev, tblLocations.locationName FROM tblLocations INNER JOIN tblLabPrograms ON (tblLocations.Abbreviation = tblLabPrograms.Building) AND (tblLocations.Abbreviation = tblLabPrograms.Building);')
for row in cursor.fetchall():
    print(row)