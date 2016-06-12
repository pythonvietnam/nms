#--------------------------------------------------
# @author: Tran Duc Loi 
# @email: loitranduc@gmail.com
# @version: 1.0
# @project: NMS - Jetpjng.com
# @community: Pythonvietnam
#--------------------------------------------------

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)-10s] %(message)s')

class CoreConfig(object):
    vhosts = [
        {'user': 'loitd', 'password': 'pwd123***fuk', 'host': 'localhost', 'port': 5672, 'name': 'default'},
        #{'user': 'loitd2', 'password': 'password', 'name': 'vh2'},
    ]

    # reloadable
    PING_INTERVAL_SECONDS = 30

    # reloadable
    URL_GET_LIST_IP = 'http://jetpjng.com/core/ip/'

    URL_POST_TRANSACTION = 'http://jetpjng.com/core/transaction/'

    def __init__(self):
        logging.info("Loading configuration ...")

    @staticmethod
    def isAvailable(vhost_name):
        for vhost in CoreConfig.vhosts:
            if vhost['name'] == vhost_name:
                return vhost
        return False

