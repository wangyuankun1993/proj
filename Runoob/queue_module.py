# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: queue_module.py
# Date: 2021/12/05 18:29:21
# Author: wangyuankun
# Function: This file is to achieve queue function!

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, thredID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Start thread:" + self.name)
        process_data(self.name, self.q)
        print("Exit thread:" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for empty the queue
while not workQueue.empty():
    pass

# Inform thread exit
exitFlag = 1

# Wait for all threads complete
for t in threads:
    t.join()
print("Exit main thread!")
