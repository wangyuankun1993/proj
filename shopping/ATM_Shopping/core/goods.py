# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: goods
# Date: 2021/04/02 00:35:14
# Author: wangyuankun
# Function: This file is to achieve goods' management!
import os, sys
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)
from conf import settings as ss
import json

class Goods(object):
    '''goods class'''

    def getGoods(self):
        '''ojtain account info'''
        try:
            with open(ss.goodsInfoFile, 'r', encoding='utf-8') as f:
                goods = json.load(f)
                # print(goods)
        except:
            print('Have no goods info!')
            goods = []
        # print(goods)
        return goods

    def setGoods(self,goods):
        '''write in goods info'''
        with open(ss.goodsInfoFile, 'w', encoding='utf-8') as f:
            json.dump(goods, f, ensure_ascii=False, indent='\t')

    def printGoods(self,goods):
        '''print goods list'''
        goods = self.getGoods()
        print(''.center(20,'-'))
        print('All goods list as follow: ')
        print(''.center(20,'-'))
        print('Index\t\tName\t\tPrice')
        print(''.center(20,'-'))
        for name, price in goods:
            print(goods.index([name,price]), '\t', name, '\t', price)
            print(''.center(20,'-'))

    def checkPrice(self,price):
        '''check the input price whether is digit'''
        if price.isdigit():
            return int(price.strip())
        else:
            print('Please input valid digit!')
            return False

    def checkName(self,name):
        '''check goods name whether exist'''
        goods = self.getGoods()
        for goodsName, price in goods:
            if name == goodsName:
                return True
        return False

    def goodsShelves(self):
        '''goods on sale'''
        name = input('Please input goods name: ').strip()
        if self.checkName(name):
            print('The goods has exist!')
            return False
        price = input('Please input price of goods: ')
        if self.checkPrice(price):
            goods = self.getGoods()
            goods.append([name,int(price)])
            print('goods\033[32;1m%s\033[0mhas been putaway! The price is: \033[32;1m%s\033[0m' % (name,int(price)))
            self.setGoods(goods)
            return True

    def goodsDelete(self):
        '''goods downshelves'''
        name = input('Please select goods need downshelves: ')
        if not self.checkName(name):
            print('Goods does not exist!')
            return False
        else:
            goods = self.getGoods()
            for goodsName, goodsPrice in goods:
                if goodsName == name:
                    goods.remove([goodsName,goodsPrice])
                    # print(goods)
                    print('Goods \033[41;1m%s\033[0mhas been downshelves!' % name)
                    self.setGoods(goods)
                    return True

    def goodsSearch(self,name):
        '''goods search query'''
        if not self.checkName(name):
            print('Goods does not exist!')
            return False
        else:
            goods = self.getGoods()
            for goodsName, goodsPrice in goods:
                if name == goodsName:
                    # obtain goods index in list
                    index = goods.index([goodsName,goodsPrice])
                    # print(index)
                    print('Goods price is: ')
                    print(name,'\t',goods[index][1])
                    return (goods, index, True)

    def goodsModify(self,name):
        '''revise goods price'''
        goods,index,Flag = self.goodsSearch(name)
        # print(Flag,'\n',goods,'\n',index)
        price = input('Please input goods price: ')
        if self.checkPrice(price):
            goods[index][1] = int(price)
            self.setGoods(goods)
            print('Goods price revised successfully!')
            print(goods[index][0],'\t','\033[32;1m%s\033[0m' % goods[index][1])
            return True

    def turnBack(self):
        '''go back last level'''
        print(''.center(15,'*'))
        print('1. Return last level')
        print('2. Exit')
        print(''.center(15,'*'))
        while True:
            choice = input('Please select: ')
            if choice == '1':
                self.goodsManagement()
            elif choice == '2':
                print('Thank you!')
                exit(-1)
            else:
                print('Invalid input, please input again!')

    def goodsManagement(self):
        '''user selection'''
        print('Please select action: ')
        print('1. Print goods list')
        print('2. Goods on shelve')
        print('3. Goods unshelve')
        print('4. Revise goods price')
        print('5. Goods query')
        while True:
            choice = input().strip()
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    # print goods list
                    self.printGoods()
                    self.turnBack()
                    break
                elif choice == 2:
                    # goods on shelve
                    self.goodsShelves()
                    self.turnBack()
                    break
                elif choice == 3:
                    # goods unshelve
                    self.goodsDelete()
                    self.turnBack()
                    break
                elif choice == 4:
                    # revise goods price
                    name = input('Please input goods name: ').strip()
                    self.goodsModify(name)
                    self.turnBack()
                    break
                elif choice == 5:
                    # goods query
                    name = input('Please input goods name: ').strip()
                    self.goodsSearch(name)
                    self.turnBack()
                    break
                else:
                    print('Invalid input, please input again!')
            else:
                print('Please input valid number!')

def run():
    goods = Goods()
    goods.goodsManagement()

if __name__ == '__main__':
    run()