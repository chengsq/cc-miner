from api import zb_market as zbm
from storage import  file_storage as fs
import time

def test_capture(times):
    zb_market = zbm.zb_market("")
    storage = fs.file_storage("tick")

    for i in range(times):
        tick = zb_market.get_tick()
        print tick
        storage.write(tick)
        time.sleep(1)




if __name__ == '__main__':

    with open("config.txt","r") as f:
        access_key = f.readline().strip()
        access_secret = f.readline().strip()
    print "access_key:",access_key
    print "access_secret:", access_secret
    test_capture(100)

    #zb_api = zba.zb_api(access_key, access_secret,"btc")
    #zb_api.query_account()
    #zb_api.get_useraddress()
    #zb_api.get_order()
    #test zb_market
    #sys.exit()
    zb_market = zbm.zb_market("")
    #zb_market.get_market()
    tick = zb_market.get_tick()
    print tick
    zb_market.get_depth(3)
    zb_market.get_trade()
    zb_market.get_kline()