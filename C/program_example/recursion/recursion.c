// /usr/bin/gcc

// File Name       : recursion.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-22 23:22:40
// Last Modified   : 2025-01-23 22:54:46
#include <stdio.h>

int fibonaci(int i)
{
    if(i == 0)
    {
        return 0;
    }
    if(i == 1)
    {
        return 1;
    }
    return fibonaci(i-1) + fibonaci(i-2);
}

int main()
{
    int i;
    for(i=0; i<10; i++)
    {
        printf("%d\t\n", fibonaci(i));
    }
    return 0;
}
