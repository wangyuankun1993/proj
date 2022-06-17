#!/bin/bash

a=10
b=20

val=`expr $a + $b`
echo "a+b: $val"

val=`expr $a - $b`
echo "a-b: $val"

val=`expr $a \* $b`
echo "a*b: $val"

val=`expr $b / $a`
echo "b/a: $val"

val=`expr $b % $a`
echo "b%a: $val"

if [ $a == $b ]
then
    echo "a等于b"
fi
if [ $a != $b ]
then
    echo "a不等于b"
fi

if [ $a -eq $b ]
then
    echo "a等于b"
else
    echo "a不等于b"
fi

if [ $a -ne $b ]
then
    echo "a不等于b"
else
    echo "a等于b"
fi

if [ $a -gt $b ]
then
    echo "a大于b"
else
    echo "a不大于b"
fi

if [ $a -lt $b ]
then
    echo "a小于b"
else
    echo "a不小于b"
fi


