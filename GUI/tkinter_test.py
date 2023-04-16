#--------------------------------------------------
# Copyright(c) : 2023
# File Name    : tkinter_test.py
# Author       : Yuankun.Wang
# Date         : 2023年04月06日 星期四 00时10分51秒
# Description  : 
#--------------------------------------------------
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Yuankun GUI')
print("My laptop resolution is %dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.update()
print("window resolution is %dx%d" % (window.winfo_width(), window.winfo_height()))
window.config(background="#6fb765")
window.geometry('%dx%d+%d+%d' % (500, 500, window.winfo_screenwidth()/2, window.winfo_screenheight()/2))
text = tk.Label(window, text="C语言中文网，欢迎您", bg="yellow", fg="red", font=('Times New Roman', 20, 'bold italic'))
#text.pack()
label = tk.Label(window, text="网址：c.biancheng.net", font=('宋体',20,'bold italic'), bg="#7CCD7C", width=30, height=5, padx=10, pady=15, borderwidth=10, relief="sunken")
#label.pack()
button1 = tk.Button(window, text="关闭", command=window.quit)
#button1.pack(side="bottom")
def click_button():
    messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')

#button2 = tk.Button(window, text='点击前往',width=20, height=5, command=click_button).pack(side="top")

tk.Label(window, text="账号：").grid(row=0)
tk.Label(window, text="密码：").grid(row=1)
e1 = tk.Entry(window)
e2 = tk.Entry(window, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def login():
    messagebox.showinfo('欢迎您到来')

tk.Button(window, text="登录", width=10, command=login).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(window, text="退出", width=10, command=window.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)

window.mainloop()
