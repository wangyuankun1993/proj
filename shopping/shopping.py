# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: shopping.py
# Date: 2021/1/17 18:32:06
# Author: wangyuankun
# Function: This file is to achieve a simply go shopping online !

salary = int(input("请用户输入工资："))
goods0 = ['iphone', 5000]
goods1 = ['mac book', 9000]
goods2 = ['coffee', 30]
goods3 = ['python book', 80]
goods4 = ['bicycle', 1000]
goods = [goods0, goods1, goods2, goods3, goods4]
shopping_cart = []

while True:
    for i,v in enumerate(goods, 0):
        print(i, v)
    goods_number = input("请输入商品编号：")
    if goods_number.isdigit():
        goods_number = int(goods_number)
        if goods_number >= 0 and goods_number < len(goods):
            price = int(goods[goods_number][1])
            if  salary < price:
                print("Sorry, the balance is insufficient!")
            else:
                salary -= price
                shopping_cart.append(goods[goods_number][0])
        else:
            print("The shoppings doesn't exist!")
    elif goods_number == 'q' or goods_number == 'Esc':
        break
    else:
        print("Invalid input!")
print("The shoppings list below: ")
for i in shopping_cart:
        print(i, list(shopping_cart).index(i))
print("The balance is %d." % (salary))
