import pyodbc
import psycopg2
import psycopg2
from psycopg2 import Error
import sys
import os

def garbage():
    print ( "Hello" )
    x = 1
    y = 2
    print( str(x) + " + " + str(y) + " = " + str( x + y ))
    for x in range ( 5, 10):
        print( x )

def getSnowflakeData():
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQLite};Direct=True;Database=mydatabase')
    cursor = cnxn.cursor()  

garbage()

def x():
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=SEI user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM my_data")
    # Retrieve query results
    records = cur.fetchall()


def getDBConnection():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(
            user="postgres",
            password="Wagw00rd",
            host="127.0.0.1",
            port="5432",
            database="SEI")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

getDBConnection();

class DBConnection():
    host = ""
    port = ""
    database = ""
    user = ""
    password = ""

     # parameterized constructor
    def __init__(self, host, port, database, user, password ):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def getConnection():
        try:
            # Connect to an existing database
            connection = psycopg2.connect(
                user="postgres",
                password="Wagw00rd",
                host="127.0.0.1",
                port="5432",
                database="SEI")

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
def connectPostgreSQL():
    connection = DBConnection( "",
                 "127.0.0.1", "5432","SEI", "postgres", "Wagwoord" ).getConnection()
