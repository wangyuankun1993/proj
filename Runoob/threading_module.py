# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: threading_module.py
# Date: 2021/12/05 17:50:34
# Author: wangyuankun
# Function: This file is to achieve threading function!

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Start thread:" + self.name)
        print_time(self.name, self.counter, 5)
        print("Exit thread:" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new thread
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

# Start new thread
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exit main thread!")
