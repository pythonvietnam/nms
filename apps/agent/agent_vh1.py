import pika
import json
import random
from time import gmtime, strftime
from pingit import PingThem

class AppAgent(object):
    def __init__(self, usr='loitd', pwd='password', host='localhost', port=5672, vhost='default'):
        creds = pika.PlainCredentials(username=usr, password=pwd)
        params = pika.ConnectionParameters(host=host, port=port, virtual_host=vhost, credentials=creds)
        self.conn = pika.BlockingConnection(parameters=params)
        self.ch = self.conn.channel()
        print("[x] Done all init ...")

        # setup consume
        self.ch.queue_declare(queue='default', durable=False, exclusive=False)
        self.ch.basic_qos(prefetch_count=100)
        self.ch.basic_consume(
            consumer_callback=self.on_consume,
            queue='default',
            no_ack=False,
        )

        print("[x] Waiting message ...")
        # Begin consuming
        try:
            self.ch.start_consuming()
        except KeyboardInterrupt:
            self.conn.close()
            print("[x] Agent interrupted by users ...")


    def on_consume(self, ch, method, props, body):
        print("[B] -------------------------------------------------- [B]")
        print("[x] Received corr_id: {0}".format(props.correlation_id))
        
        # print(body)
        body = str(body.decode('utf-8'))

        if body is None or body == 'null':
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print("[x] Done ack for None object")
            return True
        
        print("[x] Received content: {0}".format(body))

        res = self.doping(body)

        # publish back to the reply queue
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                correlation_id=props.correlation_id,
            ),
            body=res,
        )

        print("[x] Done response")
        # ack to mark the queue
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("[x] Done ack")

    def doping(self, msg):
        """
        The ping method
        :param msg:
        :return:
        """

        self._msg = json.loads(msg) # it shoulds be a list if ips

        # for demo
        # res = []
        # for el in self._msg:

        #     res.append({'i': el, 't': random.randint(0,100), 'c': strftime("%Y-%m-%d %H:%M:%S", gmtime()) })

        # real
        p = PingThem(self._msg, 200)
        res = p.run()

        return json.dumps(res)


if __name__ == '__main__':
    agent = AppAgent()
