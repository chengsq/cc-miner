import file_storage as fs
import time
import threading

class capture_data:
    def __init__(self,market):
        self.market = market
        self.data_type = ['tick','depth','trade']
        cap_dict = {}
        self.job_list = []
        for i in self.data_type:
            cap_dict[i] = fs.file_storage(i)
        self.cap_dict = cap_dict
        self.capture_count = 1
        self.count = 0
        self.last_trade_id = 0


    def capture_once(self):
        #storage = fs.file_storage("tick")
        tick = self.market.get_tick()
        self.cap_dict['tick'].write(tick)
        depth = self.market.get_depth()
        self.cap_dict['depth'].write(depth)
        trade = self.market.get_trade(self.last_trade_id)
        self.last_trade_id = trade[-1:].tid.iat[0]
        self.cap_dict['trade'].write(trade)
        print "__capture_tick"


    def capture_many(self,count):
        for i in range(0,count):
            self.capture_once()
            time.sleep(0.7)
            print "capture: %d "%(count)






