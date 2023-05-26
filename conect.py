import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123") #mydb is the object of connector class

print(mydb, "connection establish")