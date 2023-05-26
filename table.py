import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123", database="learncoding") # mydb is the object of connector class
db_cursor=mydb.cursor()  # db_cursor is the object of cursor

# db_cursor.execute("create table Emp(Roll int, name varchar(20)) ")
#print("table created")

# show tables
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)