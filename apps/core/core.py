import pika
import uuid
import json
import gevent
from gevent import monkey, Greenlet
monkey.patch_all()

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)-10s] %(message)s')
from threading import current_thread
from caller import Caller
import time
import coreconfig, importlib

class AppServer(object):
    def __init__(self, usr='loitd', pwd='123456a@', host='localhost', port=5672, vhost='vh1'):
        self.vhost = vhost
        creds = pika.PlainCredentials(username=usr, password=pwd)
        params = pika.ConnectionParameters(host=host, port=port, virtual_host=vhost, credentials=creds)
        self.is_waiting = False
        self.c = Caller()
        try:
            self.conn = pika.BlockingConnection(parameters=params)
            self.ch = self.conn.channel()
        except pika.exceptions.ProbableAccessDeniedError:
            logging.info("[AppServer] Connection error. Check configuration.")
            return None
        except:
            return None

        # declare a queue to reply
        res = self.ch.queue_declare(exclusive=True, queue='reply')
        self.reply_queue = res.method.queue # get the queue name
        self.ch.basic_consume(queue=self.reply_queue, consumer_callback=self.on_feedback, no_ack=True)
        logging.info("[AppServer] Done init ...")

    def on_feedback(self, ch, method, props, body):
        self.is_waiting = False
        logging.info("[AppServer] Received Corr_id: {0}".format(props.correlation_id))
        # logging.info(body)

        if props.correlation_id == self.corr_id:
            # call a function to insert result to db
            # format data 
            #self.vhost = self.vhost.decode('utf-8')
            body = body.decode('utf-8')
            body = json.loads(body)
            # begin inser
            toinsert = {'vhost': self.vhost, 'data': body}

            #c = Caller()

            self.c.insertIPS(coreconfig.CoreConfig.URL_POST_TRANSACTION, toinsert)
            #logging.info("The post data: {0}".format(toinsert))

            self.res = body
        return False #return false to signal to consume that you're done. other wise it continues to block

    def push(self, msg):
        """
        :param msg: list IP to ping
            msg = ['1.1.1.1', '2.2.2.2', '3.3.3.3', ]
            dumps -> encoder
            loads -> decoder
        :return:
        """
        try:
            self.corr_id = str(uuid.uuid4())
            self.res = None
            self._msg = json.dumps(msg)
            logging.info("[AppServer] Sent corr_id: {0}".format(self.corr_id))
            #logging.info("[x] Processing: {0}".format(self._msg))

            if not self.is_waiting:
                self.ch.basic_publish(
                    exchange='',
                    routing_key='default',
                    properties=pika.BasicProperties(
                        correlation_id=self.corr_id,
                        content_type='text/plain',
                        delivery_mode=2,
                        reply_to=self.reply_queue,
                    ),
                    body=self._msg,
                )
                logging.info("[AppServer] Done pushing ...")
            else:
                logging.info("[AppServer] Is waiting for the queue: {0}".format(self.is_waiting))
                pass

            # waiting
            while (self.res is None):
                self.is_waiting = True
                self.conn.process_data_events(time_limit=0)

            return self.res

        except Exception as e:
            logging.info("[AppServer] Exception while pushing message.")
            raise e
            return False


class AppCore(Greenlet):
    def __init__(self, vhost_data):
        Greenlet.__init__(self)
        self.vhost_data = vhost_data
        self.app1 = AppServer(usr=self.vhost_data['user'], pwd=self.vhost_data['password'], host=self.vhost_data['host'], port=self.vhost_data['port'], vhost=self.vhost_data['name'])
        self.c = Caller()

    def _run(self):
        current_thread().name = self.vhost_data['name']

        while 1:
            # reload config
            importlib.reload(coreconfig)
            # begin get vhosts & ips
            self.ips = self.c.getIPS(coreconfig.CoreConfig.URL_GET_LIST_IP, self.vhost_data['name'])

            # self.ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

            if self.app1 is not None:
                self.app1.push(self.ips)

            time.sleep(coreconfig.CoreConfig.PING_INTERVAL_SECONDS)



if __name__ == '__main__':
    
    d = AppCore(coreconfig.CoreConfig.vhosts[0])
    #v = AppCore({'user': 'loitd2', 'password': 'password', 'name': 'vh2'})

    d.start()
    #v.start()

    d.join()
    #v.join()