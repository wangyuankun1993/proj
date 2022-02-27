# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: atm
# Date: 2021/04/03 17:10:40
# Author: wangyuankun
# Function: This file is to achieve ATM function!
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import users as u
from conf import settings as ss

class ATM(object):
    '''ATM class'''

    @ss.log
    def deposit(self,userID,money):
        '''deposit'''
        # call Users and obtain user info
        users = u.Users().getUser()
        try:
            users[userID]['money'] = int(users[userID]['money']) + money
        except:
            # first deposit
            users[userID]['money'] = money
        # call Users and rewrite user info
        u.Users().setUser(users)
        # print('Account %s has saved %s yuan!' % (users[userID]['username'],money))
        # print('The total balance is: %s yuan.' % users[userID]['money'])
        return True

    @ss.log
    def withdrawal(self,userID,money):
        '''withdrwnal'''
        users = u.Users().getUser()
        try:
            int(users[userID]['money'])
            if money > users[userID]['money']:
                print('Balance is insufficient!')
                return False
            else:
                users[userID]['money'] -= money
        except:
            print('Balance is insufficient!')
            return False
        u.Users().setUser(users)
        # print('Account %s has withdrawaled %s yuan!' % (users[userID]['username'],money))
        return True

    @ss.log
    def transfer(self,userID,userID2,money):
        '''transfer accounts'''
        # call withdrawal, deposit and first withdrawal then deposit
        if self.withdrawal(userID,money):
            self.deposit(userID2,money)
            return True
        return False

    @ss.log
    def queryBalance(self,userID):
        '''query balance'''
        users = u.Users().getUser()
        try:
            print('Account %s balance is: \n%s yuan' % (users[userID]['username'],users[userID]['money']))
        except:
            print('Account %s balance is: \n0 yuan' % users[userID]['username'])

    def turnBack(self,userID):
        '''go back last level'''
        print(''.center(15,'*'))
        print('1. Return last level')
        print('2. Exit')
        print(''.center(15,'*'))
        while True:
            choice = input('Please input selection: ')
            if choice == '1':
                self.atmOperation(userID)
            elif choice == '2':
                print('Thank you!')
                exit(-1)
            else:
                print('Invalid input, please input again!')

    def inputMoney(self,userID):
        '''input money'''
        money = input()
        if money.isdigit():
            return int(money)
        else:
            print('Please input valid number!')
        return self.turnBack(userID)

    def atmOperation(self,userID):
        '''atm operation, main foo'''
        print('''
        Please select:
        1. Deposit
        2. Withdrawal
        3. Transfer
        4. Query
        5. Change password
        ''')
        while True:
            choice = input().strip()
            if choice == '1':
                # Deposit
                print('Please input deposit amount: ')
                money = self.inputMoney(userID)
                self.deposit(userID,money)
                print('Deposit %s yuan successfully!' % money)
                self.turnBack(userID)
                break
            elif choice == '2':
                # withdrawal
                print('Please input withdrawal amount: ')
                money = self.inputMoney(userID)
                if self.withdrawal(userID,money):
                    print('Take out %s yuan!' % money)
                self.turnBack(userID)
                break
            elif choice == '3':
                # transfer
                username = input('Please input transfer account: ')
                checkUser = u.Users().checkUser(username)
                if checkUser:
                    print('Please input transfer account: ')
                    money = self.inputMoney(userID)
                    userID2 = u.Users().getUserID(username)
                    if self.transfer(userID,userID2,money):
                        print('Transfer %s yuan to %s!' % (money,username))
                else:
                    print('Account does not exist!')
                self.turnBack(userID)
                break
            elif choice == '4':
                # query balance
                self.queryBalance(userID)
                self.turnBack(userID)
                break
            elif choice == '5':
                # change password
                u.Users().changePassword(userID)
                self.turnBack(userID)
                break
            else:
                print('Invalid input!')

def run():
    atm = ATM()
    print('Welcome log in Switzerland bank!')
    # log in verification, return userID after pass
    username, userID = u.Users().userLoggin()
    if userID:
        atm.atmOperation(userID)

if __name__ == '__main__':
    run()