import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123", database="learncoding") # mydb is the object of connector class
db_cursor=mydb.cursor()  # db_cursor is the object of cursor
# db_cursor.execute("insert into emp (Roll,name) values(%s,%s)",(20,"candy"),) # by using this we can add one value ata time

"""
db_insert="insert into emp (Roll, name) values(%s, %s)"
db_list=[(30,"gagul"),(40,"papu"),(50,"bou")]
db_cursor.executemany(db_insert,db_list)
print(db_cursor.rowcount, "record inserted")  # to see how many row have created
mydb.commit()      # to save the values in database

"""
db_cursor.execute("select * from emp")
# db_result= db_cursor.fetchall() # to show all the records using fetch all
# print(db_result)
for db_data in db_cursor.fetchall():
    print(db_data)


