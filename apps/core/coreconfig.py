import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)-10s] %(message)s')

class CoreConfig(object):
    vhosts = [
        {'user': 'loitd', 'password': 'password', 'host': 'localhost', 'port': 5672, 'name': 'default'},
        #{'user': 'loitd2', 'password': 'password', 'name': 'default2'},
    ]

    # reloadable
    PING_INTERVAL_SECONDS = 30

    # reloadable
    URL_GET_LIST_IP = 'http://localhost/core/ip/'

    URL_POST_TRANSACTION = 'http://localhost/core/transaction/'

    def __init__(self):
        logging.info("Loading configuration ...")

    @staticmethod
    def isAvailable(vhost_name):
        for vhost in CoreConfig.vhosts:
            if vhost['name'] == vhost_name:
                return vhost
        return False

