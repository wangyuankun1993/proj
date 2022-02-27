# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: thread_lock.py
# Date: 2021/12/05 18:15:19
# Author: wangyuankun
# Function: This file is to achieve thread lock and release function!

import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Start thread:" + self.name)

        # obtain lock, for synchronous thread
        threadLock.acquire()
        print_time(self.name, self.counter, 3)

        # release lock, start next thread
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

# Start new threads
thread1.start()
thread2.start()

# Add threads into thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads complete
for t in threads:
    t.join()
print("Exit main thread!")
