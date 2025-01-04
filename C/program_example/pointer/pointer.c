// /usr/bin/gcc

// File Name       : pointer.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-01 21:28:08
// Last Modified   : 2025-01-04 23:59:59
#include <stdio.h>

double getAverage(int *arr, int size);

int main()
{
    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;
    avg = getAverage(balance, 5);
    printf("Average vlaue is: %f\n", avg);
    return 0;
}

double getAverage(int *arr, int size)
{
    int i, sum = 0;
    double avg;
    for(i=0;i<size;i++)
    {
        sum += arr[i];
    }
    avg = (double)sum / size;
    return avg;
}
