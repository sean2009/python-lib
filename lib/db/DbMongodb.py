#!/usr/bin/python
'''
https://pypi.python.org/pypi/pymongo/
http://www.cnblogs.com/DxSoft/archive/2010/10/21/1857371.html
'''

import pymongo

class DbMongodb(object):
    _db_port = 27017
    _db = None
    _table = None
    
    def __init__(self,host,dbname,port = 27017):
        self._db_host = host
        self._db_name = dbname
        self._db_port = port
        
    def connect(self):
        if self._db is None:
            try:
                client  = pymongo.MongoClient(self._db_host,self._db_port)
                self._db = client[self._db_name]
            except Exception , e:
                print 'Connect Error: %s' % e
        return self._db
            
    def save(self,table_name,params):
        self.connect()    
        self._table = self._db[table_name]
        return self._table.save(params)
    
    