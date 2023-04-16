#--------------------------------------------------
# Copyright(c) : 2023
# File Name    : clock.py
# Author       : Yuankun.Wang
# Date         : 2023年04月16日 星期日 12时31分44秒
# Description  : 
#--------------------------------------------------
import tkinter as tk
import time

window = tk.Tk()
window.title('我们的时钟')
window.geometry('450x150+100+100')

def gettime():
    dstr.set(time.strftime("%H:%M:%S"))
    window.after(1000, gettime)

dstr = tk.StringVar()

lb = tk.Label(window,textvariable=dstr,fg='green',font=('微软雅黑',85))
lb.pack()
gettime()

window.mainloop()
