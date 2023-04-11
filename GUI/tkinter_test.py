#--------------------------------------------------
# Copyright(c) : 2023
# File Name    : tkinter_test.py
# Author       : Yuankun.Wang
# Date         : 2023年04月06日 星期四 00时10分51秒
# Description  : 
#--------------------------------------------------
import tkinter as tk

window = tk.Tk()
window.title('Yuankun GUI')
window.geometry('450x300')
print("My laptop resolution is %dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.update()
print("window resolution is %dx%d" % (window.winfo_width(), window.winfo_height()))
window.config(background="#6fb765")
window.attributes('-topmost', True)
window.attributes('-alpha', 1)
window["background"] = "#C9C9C9"
text = tk.Label(window, text="C语言中文网，欢迎您", bg="yellow", fg="red", font=('Times New Roman', 20, 'bold italic'))
text.pack()
button = tk.Button(window, text="关闭", command=window.quit)
button.pack(side="bottom")
window.mainloop()
