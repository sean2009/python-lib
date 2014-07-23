'''
http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/


'''

import sys,json

from lib.queue.httpsqs.HttpsqsClient import HttpsqsClient
from lib.db.DbMongodb import DbMongodb

from lib.base.mod_config import getConfig

dbhost = getConfig("main.conf","mongodb", "dbhost")


a = HttpsqsClient('192.168.0.218','1218','httpsqsmmall.com')
db = DbMongodb('192.168.0.119','testdb')
#print a.put('logtest','sdfsfsf')

def put_num(a,num):
    n = 0
    while n < num:
        str = {"tablename":"testlog","data":{"login_name":"sfdsfsf","reg_time":138176545,"mobile":13818361767,"source":"qq","n":n}}
        str = json.dumps(str,sort_keys = True,separators=(',',':'))        
        a.put('logtest',str)
        n = n + 1
put_num(a,50)
print dbhost
sys.exit(0)
#print a.get('logtest')

def red_httpsqs(a,name):
    b = a.get(name)
    while b is not None:
        yield b
        b = a.get(name)



for c in red_httpsqs(a,'logtest'):
    s = json.loads(c)
    tablename = s['tablename']
    data = s['data']
    print data
    db.save(tablename,data)
