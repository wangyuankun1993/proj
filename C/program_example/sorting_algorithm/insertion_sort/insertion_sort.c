// /usr/bin/gcc

// File Name       : insertion_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-05-12 23:04:08
// Last Modified   : 2025-05-12 23:30:47
#include <stdio.h>

void insertion_sort(int arr[], int len);

int main() {
    int arr[] = {22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
    int len = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, len);

    for (int i=0; i<len; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

void insertion_sort(int arr[], int len) {
    for (int i=1; i<len; i++) {
        int temp = arr[i];
        int j = i;
        while (j > 0 && arr[j-1] > temp) {
            arr[j] = arr[j-1];
            j--;
        }
        arr[j] = temp;
    }
}
