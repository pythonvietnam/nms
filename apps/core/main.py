#--------------------------------------------------
# @author: Tran Duc Loi 
# @email: loitranduc@gmail.com
# @version: 1.0
# @project: NMS - Jetpjng.com
# @community: Pythonvietnam
#--------------------------------------------------

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
        # reload configs
        # print("Loading configuration ...")
        # importlib.reload(coreconfig)

        # get the ips from API
        # c = Caller('http://192.168.1.176:8000/api')
        # ret = c.getIPS()
        # ret = {'90': ['192.168.1.2'], 'vh2': ['192.168.1.1', '192.168.1.2', '192.168.1.3'], 'default': ['127.0.0.1']}
        # Start all available vhost
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