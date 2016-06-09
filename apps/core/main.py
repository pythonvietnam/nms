import gevent
from gevent import monkey, Greenlet
from caller import Caller
import coreconfig
import importlib
from core import AppCore
import time, sys
monkey.patch_all()
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)-10s] %(message)s')

if __name__ == '__main__':

    try:
        tem = []
        for config in coreconfig.CoreConfig.vhosts:
                d = AppCore(config)
                d.start()
                tem.append(d)

        gevent.joinall(tem)
        # time.sleep(10)

    except KeyboardInterrupt:
        print("Application is termincated by user")
        sys.exit(0)