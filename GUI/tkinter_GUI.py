# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: tkinter_GUI.py
# Date: 2022/02/18 21:04:55
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, World!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# set window title
app.master.title('Hello World')
# main message loop
app.mainloop()
