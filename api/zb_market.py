import json, urllib2,time
import sys
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='zb.log',
                filemode='w')

class zb_market:
    def __init__(self,url,market = "btc_usdt"):
        self.url = url
        self.url = "http://api.zb.com/data/v1/"
        self.market = "market="+market
        pass

    def process_request(self,url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request, timeout=2)
            doc = json.loads(response.read())
            return doc
        except Exception, ex:
            print >> sys.stderr, 'zb request ex: ', ex
            return None

    def get_market(self):
        reqTime = (int)(time.time() * 1000)

        url = self.url + "markets"
        doc = self.process_request(url)
        print doc
        return doc


    def get_tick(self):
        reqTime = (int)(time.time() * 1000)
        url = self.url + "ticker" + "?" + self.market
        doc = self.process_request(url)
        tmp = doc['ticker']
        tmp['date'] = doc['date']

        df = pd.DataFrame([tmp])

        return df

    def get_depth(self,depth_size=3):
        reqTime = (int)(time.time() * 1000)
        depth_str = "&size=" + str(depth_size)
        url = self.url + "depth?" + self.market + depth_str
        print url
        doc = self.process_request(url)
        #tmp = doc['bids']
        #df = pd.DataFrame([tmp])
        print  doc
        return doc

    def get_trade(self):
        url = self.url + "trades"+"?" + self.market
        print url
        doc = self.process_request(url)
        #print doc
        return doc

    def get_kline(self):
        url = self.url + "kline" + "?" + self.market
        print url
        doc = self.process_request(url)
        headers = ['date', 'open', 'high', 'low', 'close','vol']
        df = pd.DataFrame(doc['data'], columns=headers)
        return df

