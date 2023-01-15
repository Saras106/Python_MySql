import csv
import database as db

PW = "password"  # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"  # considering you have installed MySQL server on your computer

RELATIVE_CONFIG_PATH = '.../config/'

USER = 'users'
PRODUCTS = 'products'
ORDER = 'orders'

connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB
db.create_and_switch_database(connection, DB, DB)
# Create the tables through python code here
s1="CREATE TABLE users (user_id varchar(5) PRIMARY KEY, user_name varchar(20),\
 user_email varchar(20), user_password varchar(20), user_address varchar(50),\
 is_vendor int)"
s2="CREATE TABLE orders (order_id int PRIMARY KEY, customer_id varchar(5),\
 vendor_id varchar(5), total_value float, order_quantity int, reward_point int,\
 FOREIGN KEY (customer_id) REFERENCES users (user_id),\
 FOREIGN KEY (vendor_id) REFERENCES users (user_id))"
s3="CREATE TABLE products (product_id varchar(5) PRIMARY KEY, product_name varchar(20),\
 product_price float, product_description varchar(15), vendor_id varchar(5),\
 emi_available varchar(5), FOREIGN KEY (vendor_id) REFERENCES users (user_id))"
db.create_table(connection,s1)
db.create_table(connection,s2)
db.create_table(connection,s3)
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

with open(RELATIVE_CONFIG_PATH + USER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    s1_1="INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s)"
    db.insert_many_records(connection,s1_1,val)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
with open(RELATIVE_CONFIG_PATH + ORDER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    s2_2="INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s)"
    db.insert_many_records(connection,s2_2,val)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """

with open(RELATIVE_CONFIG_PATH + PRODUCTS + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    s3_3="INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s)"
    db.insert_many_records(connection,s3_3,val)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
