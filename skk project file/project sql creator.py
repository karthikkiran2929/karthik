def connect():
    import time
    import mysql.connector
    global mydb
    mydb= mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "scott",
        database="bank"
        )
    global cur
    cur=mydb.cursor()
 
    print("CONNECTED TO THE SERVER SUCCESSFULLY")
    return
connect()
cur.execute("create database bank")
cur.execute("use bank")
cur.execute("create table debit ( bankname char(30),type char(2),amount bigint,interest float(4,2),rating char(2))")
cur.execute("create table expense (name char(30),amount int,entime date,fname char(30))")
cur.execute("create table salary (salary char(30),amount int)")
cur.execute("create table account3 (username varchar(30),password varchar(30))")
cur.execute("create table faze (ju integer unique)")
cur.execute("create table account4 (e_name varchar(30) unique)")
print("CREATED SUCCESSFULLY")
