# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: shopping
# Date: 2021/04/05 01:05:11
# Author: wangyuankun
# Function: This file is to achieve shopping!
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import goods as g
from core import atm as a
from conf import settings as ss
from core import users as u
import json

class ShoppingCart(object):
    '''user shopping'''

    def getBuyList(self,username):
        '''read user shopping cart list'''
        try:
            with open(ss.ShoppingCartFile(username), 'r', encoding='utf-8') as f:
                buyList = json.load(f)
                # print(buyList)
        except:
            print('Have no goods info!')
            buyList = []
        # print(buyList)
        return buyList

    def setBuyList(self,username,buyList):
        '''write user shopping cart list into file'''
        with open(ss.ShoppingCartFile(username), 'w', encoding='utf-8') as f:
            json.dump(buyList, f, ensure_ascii=False, indent='\t')

    def printBuyList(self,username):
        '''print shopping cart list'''
        sum = 0
        buyList = self.getBuyList(username)
        print(''.center(20,'-'))
        print('Shopping cart list: ')
        print(''.center(20,'-'))
        print('Name\t\tPrice')
        print(''.center(20,'-'))
        for name, price in buyList:
            print(name,'\t',price)
            sum = sum + int(price)
        print(''.center(20,'-'))
        print('Sum: \t %s' % sum)
        return sum

    def buyList(self,username,choice):
        '''Please select shopping'''
        buyList = self.getBuyList(username)
        goods = g.Goods().getGoods()
        if choice < len(goods) and choice >= 0:
            print(goods[choice])
            buyList.append(goods[choice])
            # print(buyList)
            self.setBuyList(username,buyList)
            print('Added into shopping cart successfully!')
        else:
            print('Goods does not on shelves!')
        return buyList

    def shopping(self,username,userID):
        '''shopping'''
        goods = g.Goods().printGoods()
        print(goods)
        while True:
            print("Please select, press 'q' for stopping shopping")
            choice = input().strip()
            if choice != 'q':
                if choice.isdigit():
                    choice = int(choice)
                    self.buyList(username,choice)
                else:
                    print('Please input valid number!')
            else:
                # obtain total price in shopping cart
                sum = self.printBuyList(username)
                print('Start computing!')
                n = 2
                while n >= 0:
                    password = input('Please input credit card password: ')
                    if u.Users().checkPassword(userID,password):
                        # call credit card to compute
                        if a.ATM().withdrawal(userID,sum):
                            print('Compute successfully!')
                            return True
                        else:
                            print('Compute fail!')
                    else:
                        if n != 0:
                            print('Password is incorrect! You have %s times opportunities!' % n)
                        else:
                            print('Opportunity has been used totally, compute fail!')
                    n -= 1
                # clear shopping info
                # self.setBuyList(username,buyList)
                os.remove(ss.ShoppingCartFile(username))
                return False

def run():
    s = ShoppingCart()
    print('Welcome to log in xxx website shopping mall!')
    # log in verification, return userID after pass
    username,userID = u.Users().userLoggin()
    if userID:
        s.shopping(username,userID)

if __name__ == '__main__':
    run()