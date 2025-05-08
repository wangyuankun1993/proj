// /usr/bin/gcc

// File Name       : selection_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-05-08 22:17:28
// Last Modified   : 2025-05-08 22:30:59
#include <stdio.h>

void selection_sort(int a[], int len);

int main() {
    int arr[] = {22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
    int len = sizeof(arr) / sizeof(arr[0]);
    selection_sort(arr, len);

    for (int i=0; i<len; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

void selection_sort(int a[], int len) {
    for (int i=0; i<len-1; i++) {
        int min = i;
        for (int j=i+1; j<len; j++) {
            if (a[j] < a[min]) {
                min = j;
            }
        }
        if (min != i) {
            int temp = a[min];
            a[min] = a[i];
            a[i] = temp;
        }
    }
}
