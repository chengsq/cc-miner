import file_storage as fs
import time

class capture_data:
    def __init__(self,market):
        self.market = market
        self.data_type = ['tick','kline','trade']
        cap_dict = {}
        for i in self.data_type:
            cap_dict[i] = fs.file_storage(i)



    def capture_tick(self,count = 10):
        storage = fs.file_storage("tick")

        for i in range(count):
            tick = self.market.get_tick()
            #print tick
            storage.write(tick)
            time.sleep(1)
        pass

    def capture_kline(self,count):

        for i in range(count):
            tick = self.market.get_kline()
            # print tick
            storage.write(tick)
            time.sleep(1)
        pass

    def caputure_trade(self):
        pass

