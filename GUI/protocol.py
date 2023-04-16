#--------------------------------------------------
# Copyright(c) : 2023
# File Name    : protocol.py
# Author       : Yuankun.Wang
# Date         : 2023年04月13日 星期四 00时13分22秒
# Description  : 
#--------------------------------------------------
from tkinter import Tk
from tkinter import messagebox

root = Tk()

def QueryWindow():
    if messagebox.showwarning("警告", "出现了一个错误"):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', QueryWindow)
root.mainloop()
