import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123", database="learncoding") # mydb is the object of connector class
db_cursor=mydb.cursor()  # db_cursor is the object of cursor

#delete_record="delete from emp where name=%s"
#values=("bou",)

delete_record="truncate table emp"    #to delete total records

db_cursor.execute(delete_record)
mydb.commit()
print(db_cursor.rowcount, "table deleted")