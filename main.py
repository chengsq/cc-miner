from api import zb_market as zbm
from api import zb_api as zba
from storage import  file_storage as fs
from storage import capture_data as cd
import time

def test_capture(times):
    zb_market = zbm.zb_market("")
    storage = fs.file_storage("tick")

    for i in range(times):
        tick = zb_market.get_tick()
        print tick
        storage.write(tick)
        time.sleep(1)


def test_api(access_key,access_secret):
    zb_api = zba.zb_api(access_key, access_secret, "btc")
    zb_api.query_account()
    zb_api.get_useraddress()
    zb_api.get_order()

def test_market():
    zb_market = zbm.zb_market("")
    zb_market.get_market()
    tick = zb_market.get_tick()
    print tick
    zb_market.get_depth(3)
    t = zb_market.get_trade()
    print t
    zb_market.get_kline()

def test_capture():
    zb_market = zbm.zb_market("")
    capture = cd.capture_data(zb_market)
    capture.capture_many(100)


if __name__ == '__main__':

    with open("config.txt","r") as f:
        access_key = f.readline().strip()
        access_secret = f.readline().strip()
    print "access_key:",access_key
    print "access_secret:", access_secret

    #test_api(access_key,access_secret)
    #test_market()
    test_capture()



