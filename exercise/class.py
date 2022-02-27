# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: exercise
# File Name: class
# Date: 2021/05/07 23:57:58
# Author: wangyuankun
# Function: This file is to achieve xxx!
'''
class Foo():
    __v = 'wangyuankun'

    def __init__(self):
        pass

    def show(self):
        return Foo.__v

    @staticmethod
    def stat():
        return Foo.__v

ret = Foo.stat()
print(ret)
'''

'''
class Foo():
    def __f1(self):
        return 123

    def f2(self):
        r = self.__f1()
        return r

obj = Foo()
ret = obj.f2()
print(ret)
'''

'''
class F():
    def __init__(self):
        self.gene = 123

class S(F):
    def __init__(self,name):
        self.name = 123
        self.__age = 18
        super(S,self).__init__()
    def show(self):
        print(self.name)
        print(self.__age)
        print(self.gene)

s = S('wangyuankun')
s.show()
'''

'''
class Foo():
    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')

#obj = Foo()
#obj()
Foo()()
'''

'''
class Foo():
    def __init__(self):
        pass

    def __int__(self):
        return 111

    def __str__(self):
        return 'wangyuankun'

obj = Foo()
print(obj, type(obj))
r = int(obj)
print(r)
i = str(obj)
print(i)
'''

'''
class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '%s-%s' % (self.name, self.age)

obj = Foo('wangyuankun', 18)
print(obj)
'''

'''
class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return 'xxoo'
    
    def __del__(self):
        print()

obj1 = Foo('wangyuankun', 28)
obj2 = Foo('liuchunyu', 30)

r = obj1 + obj2
print(r, type(r))
'''

'''
class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Foo('wnagyuankun', 28)
d = obj.__dict__
print(d)
f = Foo.__dict__
print(f)
'''

class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([1,2,3])


li = Foo('wangyuankun', 28)
for i in li:
    print(i)
