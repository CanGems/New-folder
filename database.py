import mysql.connector as mc

mydb=mc.connect(host ="localhost", user="root", password= "mysql123") # mydb is the object of connector class
db_cursor=mydb.cursor()

db_cursor.execute("create database learnCoding")

print("db created")