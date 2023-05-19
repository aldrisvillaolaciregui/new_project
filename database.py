from peewee import *
from peewee import Model
from peewee import MySQLDatabase



database=MySQLDatabase(
    'inventario-reparaciones',#nombre de la base de datos mysql 
     user='root',password='',
     host='localhost', port=3306 
)




class Usuario(Model):
    username=TextField(unique=True)
    password=TextField()
    
    class Meta:
        database=database
        
database.create_tables([Usuario])
    