from api import zb_api as zba
from api import zb_market as zbm
import sys
import os
import time

if __name__ == '__main__':

    with open("config.txt","r") as f:
        access_key = f.readline().strip()
        access_secret = f.readline().strip()
    # print "access_key:",access_key
    # print "access_secret:", access_secret


    zb_market = zbm.zb_market("", "btc_usdt")
    trades = list()
    tid = None
    seep_time = 1.0
    while (True):
        trade_delta = zb_market.get_trade(tid)
        num = len(trade_delta)
        tid = trade_delta[num-1]['tid']
        if num>25 and seep_time*0.9>0.1:
            seep_time = seep_time*0.9
        if num<5 and seep_time<10:
            seep_time = seep_time*1.1
        time.sleep(seep_time)
        if num>1:
            trade_delta = trade_delta[1::]
            trades.append(trade_delta)
        print num, seep_time

    print 'done'
    sys.exit()
    # zb_market.get_tick()
    # zb_market.get_depth(3)
    zb_market.get_kline()


    # amountScale, priceScale = zb_market.get_market()
    # print amountScale, priceScale


    zb_api = zba.zb_api(access_key, access_secret,"btc")
    zb_api.query_account()
    zb_api.get_useraddress()
    zb_api.get_order()
    #test zb_market