import pyodbc 

cnxn_str = ("Driver={SQL Server};"
            "Server=ANORTJE-5CD1326;"
            "Database=AdventureWorks;"
            "Trusted_Connection=yes;"
            "uid=anortje;pwd=Wagw00rd")

cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cursor.execute("SELECT * FROM [AdventureWorks].[Person].[Address] where city = 'Bothell';") 
row = cursor.fetchone() 
while row: 
    print(row)
    row = cursor.fetchone()
