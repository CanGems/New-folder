import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123") #mydb is the object of connector class
db_cursor=mydb.cursor()

update_query="update learncoding.emp set Roll=%s where name=%s"
set_value=(11, "bou")
db_cursor.execute(update_query,set_value)
mydb.commit()
print("update sucessful")