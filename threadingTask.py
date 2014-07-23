import Queue, threading, time, json, datetime

from lib.queue.httpsqs.HttpsqsClient import HttpsqsClient
from lib.db.DbMongodb import DbMongodb

httpsqs = HttpsqsClient('192.168.0.218','1218','httpsqsmmall.com')
queue = Queue.Queue()
db = DbMongodb('192.168.0.119','testdb')

class ThreadGetHttpSqs(threading.Thread):
    def __init__(self, httpsqs, queue):
        threading.Thread.__init__(self)
        self.httpsqs = httpsqs
        self.queue = queue
    
    def run(self):
        while True:
            data = self.httpsqs.get('logtest')
            if data is not None:
                self.queue.put(data)
                print "id:%s, %s" % (self.getName(),data)
            else:
                time.sleep(3)
            
            
            
class ThreadInsertDB(threading.Thread):
    def __init__(self, queue, db):
        threading.Thread.__init__(self)
        self.queue = queue
        self.db = db
        
    def run(self):
        while True:
            chunk = self.queue.get()
            s = json.loads(chunk)
            tablename = s['table']
            data = s['data']
            self.db.save(tablename,data)
            self.queue.task_done()
            
            
def main():
    
    for i in range(2):
        t = ThreadGetHttpSqs(httpsqs,queue)
        #t.setDaemon(True)
        t.start()
    
    for i in range(5):
        t = ThreadInsertDB(queue, db)
        #t.setDaemon(True)
        t.start()
    
main()
