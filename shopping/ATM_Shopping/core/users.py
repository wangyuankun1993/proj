# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: users
# Date: 2021/03/26 23:30:43
# Author: wangyuankun
# Function: This file is to achieve little function!
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from conf import settings as ss
import json

class Users(object):
    '''user class, manage user interface'''

    def getUser(self):
        '''obtain account information'''
        try:
            with open(ss.userInfoFile, 'r', encoding='utf-8') as f:
                users = json.load(f)
                #print(users)
        except:
            print('Have no user info!')
            users = {}
        return users

    def setUser(self,users):
        '''rewrite account information'''
        with open(ss.userInfoFile, 'w') as f:
            json.dump(users, f, indent='\t')

    def checkUser(self,username):
        '''check user whether exist'''
        users = self.getUser()
        for userID in users.keys():
            if username == users[userID]['username']:
                #print('The account already exist!')
                return True
        return False

    def getUserID(self,username):
        '''obtain ID from account'''
        users = self.getUser()
        for userID in users.keys():
            if username == users[userID]['username']:
                return userID
        print("The account does't exist!")
        return self.turnBack()

    def addUser(self,username,password,phone=None,limit=ss.creditLimit,isLock=False):
        '''add account'''
        users = self.getUser()
        '''dict key automaticly plus 1'''
        max_id = '000000'
        if users != {}:
            max_id = max(users.keys())
        userID = str(int(max_id) + 1).zfill(6) # id plus 1 and supply 6 bits
        users[userID] = {
            'username':username,
            'password':password,
            'phone':phone,
            'limit':limit,
            'isLock':isLock
        }
        self.setUser(users)
        print(''.center(50,'#'))
        print('Account \033[42;1m%s\033[0madd success' % users[userID]['username'])
        print('Account Name: %s' % users[userID]['username'])
        print('Phone Number: %s' % users[userID]['phone'])
        print('Credit Limit: %s' % users[userID]['limit'])
        print(''.center(50,'#'))
        return True

    def delUser(self,userID):
        '''logout account'''
        users = self.getUser()
        try:
            print('Account \033[41;1m%s\033[0mdelete success' % users[userID][
                'username'])
            users.pop(userID)
        except:
            print("Account doesn't exist!")
            return False
        self.setUser(users)
        return True

    def frozenUser(self,userID):
        '''frozen account'''
        users = self.getUser()
        users[userID]['isLock'] = True
        self.setUser(users)
        print('Account %s has been frozen!' % users[userID]['username'])

    def thawUser(self,userID):
        '''thaw account'''
        users = self.getUser()
        users[userID]['isLock'] = False
        self.setUser(users)
        print('Account %s has been thawed!' % users[userID]['username'])

    def userLoggin(self):
        '''user log in verification'''
        for i in range(1,4):
            username = input('Please input username: ')
            if self.checkUser(username):
                userID = self.getUserID(username)
                users = self.getUser()
                if users[userID]['isLock']:
                    print('The account has been frozen, please contact admin!')
                    exit(1)
                password = input('Please input password: ')
                if self.checkPassword(userID,password):
                    return username,userID
                else:
                    print('Password incorrect!')
            else:
                print('Account not exist!')
        print('Action is too frequently!')
        return False,False

    def checkPassword(self,userID,password):
        '''check password whether correct'''
        users = self.getUser()
        if password == users[userID]['password']:
            return True
        else:
            return False

    @ss.log
    def changePassword(self,userID):
        '''change password'''
        for i in range(1,4):
            old_passwd = input('Please input old password: ')
            # check old password whether correct
            check = self.checkPassword(userID,old_passwd)
            if check:
                for j in range(1,4):
                    if j == 3:
                        print('Action too frequently!')
                        return False
                    new_passwd1 = input('Please input new password: ')
                    if len(new_passwd1) < 8:
                        print('Password can not less than 8 words!')
                        continue
                    if new_passwd1 == old_passwd:
                        print('New password can not same with old password!')
                        continue
                    new_passwd2 = input('Please confirm the new password: ')
                    if new_passwd1 != new_passwd2:
                        print('The two password inconformity!')
                        continue
                    else:
                        users = self.getUser()
                        users[userID]['password'] = new_passwd1
                        self.setUser(users)
                        print('Password changed successfully!')
                        return True
            else:
                print('Old password is incorrect!')
        print('Action is too frequently!')
        return False

    def changePhone(self,userID,phone):
        '''change phone number'''
        users = self.getUser()
        users[userID]['phone'] = phone
        self.setUser(users)
        print('Phone revised successfully!')
        print('Account name: %s' % users[userID]['username'])
        print('Phone: %s' % users[userID]['phone'])

    def changeLimit(self,userID,limit):
        '''revise account limit'''
        users = self.getUser()
        users[userID]['limit'] = limit
        self.setUser(users)
        print('Account %s creditLimit has been updated to %s.' % (users[userID]['username'],users[userID]['limit']))

    def turnBack(self):
        '''return last level'''
        print(''.center(15,'*'))
        print('1. return last level')
        print('2. exit')
        print(''.center(15,'*'))
        while True:
            choice = input('Please choice: ')
            if choice == '1':
                self.userManagement()
            elif choice == '2':
                print('Thank you!')
                exit(1)
            else:
                print('Invalid inputs, please input again!')

    def userManagement(self):
        '''account management, main entrance foo'''
        print('''
        Please choice user management action:
        1. Account info query
        2. Add new account
        3. Delete account
        4. Change password
        5. Change phone number
        6. Frozen account
        7. Thaw account
        8. Change account credit limit
        ''')
        while True:
            choice = input().strip()
            if choice.isdigit():
                if choice == '1':
                    # account info query
                    users = self.getUser()
                    print(''.center(50,'#'))
                    for i in users.keys():
                        print('Account name: %s' % users[i]['username'])
                        print('Phone number: %s' % users[i]['phone'])
                        print('Credit limit: %s' % users[i]['limit'])
                        print(''.center(50,'#'))
                    self.turnBack()
                    break
                elif choice == '2':
                    # add new account
                    username = input('Please input username: ')
                    # check username whether exist
                    if self.checkUser(username):
                        print('The account already exist!')
                        self.turnBack()
                        break
                    password = input('Please input password: ')
                    phone = input('Please input phone number: ')
                    self.addUser(usename,password,phone)
                    self.turnBack()
                    break
                elif choice == '3':
                    # delete account
                    username = input('Please input account: ')
                    userID = self.getUserID(username)
                    self.delUser(userID)
                    self.turnBack()
                    break
                elif choice == '4':
                    # change password
                    username = input('Please input account name need to change password: ')
                    userID = self.getUserID(username)
                    self.changePassword(userID)
                    self.turnBack()
                    break
                elif choice == '5':
                    # change phone number
                    username = input('Please input account name need to change phone: ')
                    userID = self.getUserID(username)
                    phone = input('Please input new phone: ')
                    self.changePhone(userID,phone)
                    self.turnBack()
                    break
                elif choice == '6':
                    # frozen account
                    username = input('Please input account name need to freeze: ')
                    userID = self.getUserID(username)
                    self.frozenUser(userID)
                    self.turnBack()
                    break
                elif choice == '7':
                    # thaw account
                    username = input('Please input account name need to thaw: ')
                    userID = self.getUserID(username)
                    self.thawUser(userID)
                    self.turnBack()
                    break
                elif choice == '8':
                    # change account credit limit
                    username = input('Please input account name need to chagne credit limit: ')
                    userID = self.getUserID(username)
                    limit = input('Please input credit limit that need to change: ')
                    if limit.isdigit():
                        self.changeLimit(userID,limit)
                    else:
                        print('Input invalid, updated fail!')
                    self.turnBack()
                    break
                else:
                    print('Please input valid number!')
            else:
                print('Please input valid number!')

def run():
    users = Users()
    users.userManagement()

if __name__ == '__main__':
    run()