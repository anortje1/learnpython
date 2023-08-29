import snowflake.connector

#open a database connection
ctx = snowflake.connector.connect(
    user = "anortje",
    password = "Fokkak10",
    account= "ulmffhc-bq09859"
    #, region = "us-east-2"
    #, Role =  "ACCOUNTADMIN"
    ,Warehouse =  "COMPUTE_WH"
    #,database =  "DEMO"
    #, schema = "Public"
    )

#create a cursor object
cs = ctx.cursor()

sql_query = '''    
    SELECT *
    FROM demo.public.users '''
    
print( sql_query )

cs.execute(sql_query)

data = cs.fetchall()
print( data )
for row in data:
    print( row )

print( "All done")



