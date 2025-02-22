// /usr/bin/gcc

// File Name       : bubble_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-22 21:40:05
// Last Modified   : 2025-02-22 22:22:30
#include <stdio.h>

void bubble_sort(int arr[], int len);

int main()
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int len = sizeof(arr) / sizeof(arr[0]);

    bubble_sort(arr, len);

    for(int i=0; i<len; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}

void bubble_sort(int arr[], int len)
{
    for(int i=0; i<len-1; i++) // count
    {
        for(int j=0; j<len-1-i; j++) // array index
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}
