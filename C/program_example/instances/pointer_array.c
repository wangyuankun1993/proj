// /usr/bin/gcc

// File Name       : pointer_array.c
// Author          : Yuankun.Wang
// Created Time    : 2025-10-12 20:13:31
// Last Modified   : 2025-10-12 20:18:27
#include <stdio.h>

int main() {
    int data[5], i;
    printf("Input element: ");
    for (i=0; i<5; ++i) {
        scanf("%d", data + i);
    }
    printf("Output element: \n");
    for (i=0; i<5; ++i) {
        printf("%d\n", *(data + i));
    }
    return 0;
}
