#--------------------------------------------------
# @author: Tran Duc Loi 
# @email: loitranduc@gmail.com
# @version: 1.0
# @project: NMS - Jetpjng.com
# @community: Pythonvietnam
#--------------------------------------------------

from threading import Thread
from queue import Queue

import subprocess
import gevent
# from gevent import monkey, Greenlet
# monkey.patch_all()
import logging
logging.basicConfig(level=logging.INFO, format='(%(threadName)-10s) %(message)s', )
import time
from time import gmtime, strftime

# from datetime import datetime
# from pytz import timezone


class PingIt(object):
    def __init__(self):
        pass

    def get_cur_time(self):
        # get the time based on local time of the server
        # return strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # print(time.localtime(time.time()))
        # print(time.gmtime())
        # print(datetime.utcnow())
        return strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        
        # hn = timezone('Asia/Saigon')
        # localdt = hn.localize(datetime.now())
        # return localdt.strftime('%Y-%m-%d %H:%M:%S %Z%z')


    def doping(self, target, numofpack=2, cmdtimeout=2, defaultdie=999):
        # logging.info("Ping check to: {0}".format(target))
        self.command = "ping -c {0} -w {1} {2}".format(numofpack, cmdtimeout, target)
        self.target = target
        self.defaultdie = defaultdie
        # p = subprocess.check_output(self.theCommand(target), shell=True)
        p = subprocess.Popen(['ping', target, '-c', str(numofpack), '-w', str(cmdtimeout)], stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        rt = p.wait()
        self.msg = p.stdout.read().decode("utf-8")
        # print(msg)

        if rt == 1 or rt == 0:
            d = self.getResult()
        else:
            print(rt)
            print(self.msg)
            d = {"ip": self.target, "t": self.defaultdie, 'c': self.get_cur_time() }

        print(d)
        return d

    def getResult(self):
        # logging.info(self.msg)

        if (self.msg.find(r"rtt min/avg/max/mdev =") != -1):
            logging.info("good quality!!!")
            time = float(self.msg.split("rtt min/avg/max/mdev = ")[1].split("/")[1])

            # constraint to 99
            if time > self.defaultdie:
                time = self.defaultdie

            return {"ip": self.target, "t": time, "c": self.get_cur_time() }
        else:
            logging.info("unreachable or poor quality")
            return {"ip": self.target, "t": self.defaultdie, "c": self.get_cur_time() }

class PingThem():
    def __init__(self, targets, maxthreads=100):
        self.q1 = Queue(maxsize=0)
        self.q2 = Queue(maxsize=0)
        self.maxthreads = maxthreads if len(targets) >= maxthreads else len(targets)
        

        for target in targets:
            self.q1.put(target)
        logging.info("Done adding all targets")

        print(self.q1.qsize())


    def worker(self):
        while 1:
            i = self.q1.get()
            # logging.info("Got value from queue: {0}".format(i))
            # quit cond
            if i is None:
                break

            p = PingIt()
            r = p.doping(i)

            self.q2.put(r)

            self.q1.task_done()

    def run(self):
        print("Will start {0} threads for checking ...".format(self.maxthreads))
        allts = []
        for i in range(self.maxthreads):
            t = Thread(target=self.worker)
            t.start()
            allts.append(t)

        self.q1.join()

        for i in range(self.maxthreads):
            self.q1.put(None)

        for t in allts:
            t.join()

        # check q2
        logging.info(self.q2.qsize())

        ret = []
        for j in range(self.q2.qsize()):
            i = self.q2.get()
            if i is None:
                break
            ret.append(i)

        return ret


    

if __name__ == '__main__':
    targets = [
        'vnexpress.net', 'megacard.vn', 'shipantoan.vn', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
        # '1.1.1.1', '2.2.2.2', '3.3.3.3', '8.8.8.8', '127.0.0.1', 'localhost', 'google.com', 'dantri.com.vn', 
    ]
    
    # p = PingThem(targets, 300)
    # x = p.run()
    # print(x)

    p = PingIt()
    print(p.get_cur_time())
    # p.doping('127.0.0.1')










