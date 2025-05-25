// /usr/bin/gcc

// File Name       : merge_sort.c
// Author          : Yuankun.Wang
// Created Time    : 2025-05-25 22:30:25
// Last Modified   : 2025-05-25 23:04:42
#include <stdio.h>
#include <stdlib.h>

int min(int x, int y);
void merge_sort(int arr[], int len);

int main() {
    int arr[] = {22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
    int len = sizeof(arr) / sizeof(arr[0]);
    merge_sort(arr, len);
    for (int i=0; i<len; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

int min(int x, int y) {
    return x < y ? x : y;
}

void merge_sort(int arr[], int len) {
    int* a = arr;
    int* b = (int*) malloc(len * sizeof(int));
    if (b == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int seg=1; seg<len; seg+=seg) {
        for (int start=0; start<len; start+=seg+seg) {
            int low = start;
            int mid = min(start+seg, len);
            int high = min(start+seg+seg, len);
            int k = low;
            int start1 = low, end1 = mid;
            int start2 = mid, end2 = high;
            while (start1 < end1 && start2 < end2) {
                b[k++] = a[start1] < a[start2] ? a[start1++] : a[start2++];
            }
            while (start1 < end1) {
                b[k++] = a[start1++];
            }
            while (start2 < end2) {
                b[k++] = a[start2++];
            }
        }
        int* temp = a;
        a = b;
        b = temp;
    }
    if (a != arr) {
        for (int i = 0; i < len; i++) {
            b[i] = a[i];
        }
        b = a;
    }
    free(b);
}
