# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: check_server
# File Name: check_server_new
# Date: 2022/08/20 17:03:24
# Author: wangyuankun
# Function: This file is to achieve !
import psutil
import os, datetime, time

record_interval = 0.5

def get_cpu_info():
    # cpu
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_avg = str(psutil.cpu_percent(interval=record_interval)) + "%"

    # memory
    mem = psutil.virtual_memory()
    mem_total = round(mem.total/1024/1024/1024, 1)
    mem_avg = str(mem.percent) + "%"

    # disk
    disk = psutil.disk_usage('/')
    disk_total = round(disk.total/1024/1024/1024, 1)
    disk_avg = str(disk.percent) + "%"

    return (cpu_cores, cpu_avg, mem_total, mem_avg, disk_total, disk_avg)

def main():
    now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    fname = now + r'-report.csv'
    with open('%s' % fname, 'w') as f:
        title_str = "Time, CPU_cores, CPU_avg, Mem_total, Mem_avg, Disk_total, Disk_avg"
        print(title_str)
        f.write("Time, CPU_cores, CPU_avg, Mem_total, Mem_avg, Disk_total, Disk_avg" + "\n")
        for i in range(999999):
            info = get_cpu_info()
            tmp_str = "%5s, %5s, %5s, %5s, %5s, %5s, %5s" % (i*record_interval, info[0], info[1], info[2], info[3], info[4], info[5])
            print(tmp_str)
            f.write(tmp_str + "\n")

if __name__ == '__main__':
    main()