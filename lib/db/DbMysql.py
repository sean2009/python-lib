'''
db = DbMysql('192.168.0.216','hmeai','hmeai','hm_bossadmin',33306)
list = db.fetchAll('select id,admin_name from eai_power_login where admin_name = %s order by id desc limit 10','hmadmin')
#print list
for val in list:
    print '%d %s' % (val['id'],val['admin_name'])
'''

import MySQLdb

class DbMysql(object):
    _conn,_cursor = None,None
    
    def __init__(self,host,user,passwd,dbname,port = 3306,charset = 'utf8'):
        self.db_host = host
        self.db_user = user
        self.db_passwd = passwd
        self.db_name = dbname
        self.db_port = port
        self.db_charset = charset
        
    def connect(self):
        if self._conn is None:
            try:
                self._conn = MySQLdb.connect(self.db_host,self.db_user,self.db_passwd,self.db_name,self.db_port,self.db_charset)
                self._cursor=self._conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            except  Exception , e:
                print 'Connect Error: %s' % e
        
    
    def execute(self,sql,params = None):
        try:
            self.connect()
            return self._cursor.execute(sql,params)
        except Exception as e:
            print 'Execute Mysql Error: (%s) %s' % (sql, e)
    
    def commit(self):
        if self._conn is None:
            return False
        return self._conn.commit()
    
    def fetchAll(self,sql = None,params = None):
        if sql is not None:
            self.execute(sql,params)
        return self._cursor.fetchall()
    
    def fetchOne(self,sql = None,params = None):
        if sql is not None:
            self.execute(sql,params)
        return self._cursor.fetchone()    
    
    def close(self):
        if self._cursor is not None:
            self._cursor.close()
            self._conn.close()
    
    def __del__(self):
        self.close()
        

    
