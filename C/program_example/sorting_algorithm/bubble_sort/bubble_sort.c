// /usr/bin/gcc

// File Name       : bubble_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-22 21:40:05
// Last Modified   : 2025-03-08 22:35:03
#include <stdio.h>

void bubble_sort(int arr[], int len);

int main()
{
    int arr[] = { 2, 1, 3, 4, 5, 6 };
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
        int flag = 0;
        for(int j=0; j<len-1-i; j++) // array index
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                flag = 1;
            }
        }
        printf("flag value is: %d!!!\n", flag);
        if(flag == 0)
        {
            break;
        }
    }
}
