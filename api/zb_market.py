import json,time
import urllib   
import urllib2 
import sys
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='zb.log',
                filemode='w')

class zb_market:
    def __init__(self,url,market = "btc_usdt"):
        self.url = url
        self.url = "http://api.zb.com/data/v1/"
        self.market = market
        pass

    def process_request(self,url,values):
        try:  
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            doc = response.read()
            return doc
        except Exception, ex:
            print >> sys.stderr, 'zb request ex: ', ex
            return None

    def get_market(self):
        reqTime = (int)(time.time() * 1000)
        url = self.url + "markets"
        doc = self.process_request(url)
        try:
            detail = doc[self.market]
            amountScale = detail['amountScale']
            priceScale = detail['priceScale']
        except:
            print 'Parse market error!'
        return amountScale, priceScale


    def get_tick(self):
        reqTime = (int)(time.time() * 1000)
        url = self.url + "ticker" + "?market=" + self.market
        print url
        doc = self.process_request(url)
        return doc

    def get_depth(self,depth_size):
        reqTime = (int)(time.time() * 1000)
        depth_str = "size=" + str(depth_size)
        url = self.url + "depth" + "?market=" + self.market+depth_str
        doc = self.process_request(url)
        return doc

    def get_trade(self, tid):
        url = self.url + "trades"
        if tid == None:
            values = {'market' : self.market} 
        else:
            values = {'market' : self.market, 'since' : tid} 
        doc = self.process_request(url, values)
        return eval(doc)

    def get_kline(self):
        url = self.url + "kline" + "?market=" + self.market + '&type=1min'
        doc = self.process_request(url)
        print eval(doc)['moneyType']
        print np.array(eval(doc)['data'])
        return doc

