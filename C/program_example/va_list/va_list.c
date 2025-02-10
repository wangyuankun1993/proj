// /usr/bin/gcc

// File Name       : va_list.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-10 22:26:24
// Last Modified   : 2025-02-10 22:35:54
#include <stdio.h>
#include <stdarg.h>

double average(int num, ...)
{
    va_list valist;
    double sum = 0.0;
    int i;

    /*initial valist for num variation*/
    va_start(valist, num);

    /*access variation for valist*/
    for(i=0; i<num; i++)
    {
        sum += va_arg(valist, int);
    }

    /*clear memory for valist*/
    va_end(valist);
    return sum/num;
}

int main()
{
    printf("Average of 2, 3, 4, 5 = %f\n", average(4, 2, 3, 4, 5));
    printf("Average of 5, 10, 15 = %f\n", average(3, 5, 10, 15));
}
