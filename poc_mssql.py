import pyodbc

from prettytable import PrettyTable

# specifiy odbc driver
dbcon = pyodbc.connect('DRIVER={SQL Server};SERVER=10.180.22.134;DATABASE=reporting-j2w;UID=webuser;PWD=Passw0rd')

# create cursor
cursor = dbcon.cursor()

# make a query
cursor.execute("select name, description, lastmodified from roles")

# get all result
rows = cursor.fetchall()

# prepare table
table = PrettyTable(['Role name', 'Role Description', 'Last modified'])

for row in rows:
    table.add_row([row.name, row.description, row.lastmodified])

#print it
print (table)
