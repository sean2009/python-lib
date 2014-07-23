import MySQLdb
from lib.db.mysql.skylark import Database, Model, Field, PrimaryKey, ForeignKey

Database.set_dbapi(MySQLdb)
Database.config(db='mydb', user='root', passwd='')

class BaseModel(Model):
    id = Field(True)