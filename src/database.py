import mysql.connector
import random
import time
import datetime


# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    # Implement the logic to create the server connection
    conn=mysql.connector.connect(host=host_name,user=user_name,password=user_password)
    return conn

# This method will create the database and make it an active database
def create_and_switch_database(connection, db_name, switch_db):
    # For database creatio nuse this method
    # If you have created your databse using UI, no need to implement anything
    mycursor=connection.cursor()
    mycursor.execute("SHOW DATABASES")
    lst=mycursor.fetchall()
    if (db_name,) not in lst:
        stri="CREATE DATABASE {}".format(db_name)
        mycursor.execute(stri)
        srt="USE {}".format(db_name)
        mycursor.execute(srt)
    else:
        srt="USE {}".format(switch_db)
        mycursor.execute(srt)
# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    pass


# Use this function to create the tables in a database
def create_table(connection, table_creation_statement):
    statement=table_creation_statement
    mycursor=connection.cursor()
    mycursor.execute("SHOW TABLES")
    tb=mycursor.fetchall()
    lst=statement.split()
    n=lst[2]
    if (str(n),) in tb:
        return None
    else:
        mycursor.execute(statement)
    
# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    # This method will perform creation of the table
    # this can also be used to perform single data point insertion in the desired table
    mycursor=connection.cursor()
    mycursor.execute(query)
    connection.commit()
    mycursor.close()
    
# retrieving the data from the table based on the given query
def select_query(connection, query):
    # fetching the data points from the table 
    mycursor=connection.cursor()
    mycursor.execute(query)
    res=mycursor.fetchall()
    for x in res:
        print(x)


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    mycursor=connection.cursor()
    mycursor.executemany(sql,val)
    connection.commit()
    mycursor.close()
    
