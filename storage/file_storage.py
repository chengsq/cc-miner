import pandas as pd
import os
import time

class file_storage:
    def __init__(self,prefix):
        cwd_path = os.getcwd()
        storage_path = os.path.join(cwd_path,"csv_storage")
        if not os.path.exists(storage_path):
            os.mkdir(storage_path)

        storage_name = prefix+time.strftime("_%Y-%m-%d %H:%M:%S",time.gmtime()) + '.csv'
        self.storage_name = os.path.join(storage_path,storage_name)
        self.count = 0

    def write(self,item):
        if self.count == 0:
            item.to_csv(self.storage_name, header='column_names')
        else:  # else it exists so append without writing the header
            item.to_csv(self.storage_name, mode='a', header=False)
        self.count += 1

