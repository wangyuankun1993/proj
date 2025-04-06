// /usr/bin/gcc

// File Name       : bubble_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-22 21:40:05
// Last Modified   : 2025-04-06 13:20:43
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
    int swapped;
    int end_range = len - 1;
    for (int i=0; i<len-1; i++) // count
    {
        swapped = 0;
        for (int j=0; j<end_range; j++) // array index
        {
            if(arr[j] > arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                swapped = 1;
            }
        }
        if (swapped == 0) {
            break;
        }
        end_range--;
    }
}
