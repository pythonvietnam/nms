#--------------------------------------------------
# @author: Tran Duc Loi 
# @email: loitranduc@gmail.com
# @version: 1.0
# @project: NMS - Jetpjng.com
# @community: Pythonvietnam
#--------------------------------------------------

import requests
import json

# import mylog
import logging
# mylog.initialize_logger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)-10s] %(message)s')


class Caller(object):
    def __init__(self):
        #self.url = url
        pass


    def getIPS(self, url, vhost=None):
        try:
            r = requests.get(url, data={'vhost': vhost})
            if r.status_code == 200:
                #print(r.json())
                if vhost == None:
                    return r.json()
                else:
                    for k,v in r.json().items():
                        if k == vhost:
                            return v
        except requests.exceptions.ConnectionError as e:
            logging.error("[Caller] ConnectionError while Get IPs: {0}".format(e))
        except Exception as e:
            logging.error("[Caller] Get IPs failed: {0}".format(e))
        return False


    def insertIPS(self, url, msg):
        print("[Caller] Begin posting data: {0}".format(msg))
        # print(json.loads(msg['data']))
        logging.info("[Caller] Begin posting data")
        # msg = {'default': [{'ip': '1.1.1.1', 't': '9', 'date': '2016-05-16 14:12:12'}, {'ip': '1.1.1.1', 't': '9', 'date': '2016-05-16 14:12:22'}]},
        r = requests.post(url, json.dumps(msg))
        logging.info("[Caller] Done posting data")
        pass



if __name__ == '__main__':
    c = Caller('http://jetpjng.com/core/transaction/')
    # c.getIPS()
    fakedata = {'vhost': 'default', 'data': '[{"ip": "dantri.com", "c": "2016-06-07 08:03:59", "t": 68.322}, {"ip": "ecoit.asia", "c": "2016-06-07 08:03:59", "t": 56.216}, {"ip": "mail.vnptepay.com.vn", "c": "2016-06-07 08:03:59", "t": 57.435}, {"ip": "matbao.net", "c": "2016-06-07 08:03:59", "t": 59.581}, {"ip": "netnam.vn", "c": "2016-06-07 08:03:59", "t": 56.446}, {"ip": "vnptepay.com.vn", "c": "2016-06-07 08:03:59", "t": 59.463}, {"ip": "coursebridge.org", "c": "2016-06-07 08:03:59", "t": 0.57}, {"ip": "www.tecmint.com", "c": "2016-06-07 08:03:59", "t": 99}, {"ip": "namecheap.com", "c": "2016-06-07 08:03:59", "t": 99}, {"ip": "facebook.com", "c": "2016-06-07 08:03:59", "t": 99}, {"ip": "vietsoftware.com", "c": "2016-06-07 08:03:59", "t": 55.705}, {"ip": "gooogle.com.vn", "c": "2016-06-07 08:03:59", "t": 99}, {"ip": "vnexpress.net", "c": "2016-06-07 08:04:00", "t": 99}, {"ip": "shipantoan.vn", "c": "2016-06-07 08:04:00", "t": 99}, {"ip": "thanhtoan247.vn", "c": "2016-06-07 08:04:00", "t": 99}, {"ip": "megacard.vn", "c": "2016-06-07 08:04:05", "t": 99}]'}
    c.insertIPS(fakedata)