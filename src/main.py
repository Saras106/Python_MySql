import time
import database as db

# Driver code
if __name__ == "__main__":
    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "password"  # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever
    # you like.
    LOCALHOST = "localhost"
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)
    # creating the schema in the DB 
    db.create_and_switch_database(connection, DB, DB)

    # Start implementing your task as mentioned in the problem statement 
    # Implement all the test cases and test them by running this file

print("INSERT 5 OPERATIONS TO orders TABLE: ")
time.sleep(1)
new_val=[]
t1=('101', '7', '3', '23162.0', '4', '100')
new_val.append(t1)
t2=('102', '13', '5', '39127.0', '1', '200')
new_val.append(t2)
t3=('103', '12', '1', '112361.0', '4', '300')
new_val.append(t3)
t4=('104', '9', '4', '61237.0', '2', '100')
new_val.append(t4)
t5=('105', '11', '2', '45563.0', '3', '100')
new_val.append(t5)
statement="INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s)"
db.insert_many_records(connection,statement,new_val)
print("VALUES INSERTED SUCCESSFULLY")
print("\n\nPRINT orders TABLE: ")
time.sleep(1)
query="SELECT * FROM orders"
db.select_query(connection,query)
print("\n\nMAX ORDER VALUE")
time.sleep(1)
query_1="SELECT * FROM orders WHERE total_value=(SELECT MAX(total_value) FROM orders)"
db.select_query(connection,query_1)
print("\n\nMIN ORDER VALUE")
time.sleep(1)
query_2="SELECT * FROM orders WHERE total_value=(SELECT Min(total_value) FROM orders)"
db.select_query(connection,query_2)
#print("\nMAX & MIN TOGETHER: ")
#quer4="SELECT * FROM orders WHERE total_value=(SELECT MAX(total_value) FROM orders)\
# or total_value=(SELECT MIN(total_value) FROM orders)"
#db.select_query(connection,quer4)
print("\n\nPRINT ORDERS WITH TOTAL VALUE GREATER THAN AVERAGE: ")
time.sleep(1)
query_3="SELECT * FROM orders WHERE total_value > (SELECT AVG(total_value) FROM orders) ORDER BY total_value"
db.select_query(connection,query_3)
print("\n\nCREATE NEW TABLE customer_leaderboard: ")
time.sleep(1)

sx="CREATE TABLE customer_leaderboard (customer_id varchar(5) primary key,\
 total_value float, customer_name varchar(20), customer_email varchar(30))"
db.create_table(connection,sx)
n_qr="select o.customer_id,o.total_value,u.user_name,u.user_email from\
 orders o inner join users u on o.customer_id=u.user_id where o.total_value=(select\
 max(total_value) from orders d where d.customer_id=o.customer_id);"
cur=connection.cursor()
cur.execute(n_qr)
res=cur.fetchall()
n=list(res)
n_s="INSERT INTO customer_leaderboard VALUES (%s,%s,%s,%s)"
db.insert_many_records(connection,n_s,n)
n_ss="SELECT * FROM customer_leaderboard ORDER BY customer_id"
db.select_query(connection,n_ss)
