#! /usr/bin/python3
# author: yuankun.wang
# date: 2021/01/02
# function: This grogram is to generate multiplication table.


j = 1
while j < 10:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (i,j,i*j), end=" ")
        i += 1
    j += 1
    print()
