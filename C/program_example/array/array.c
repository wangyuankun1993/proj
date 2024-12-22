// /usr/bin/gcc

// File Name       : array.c
// Author          : Yuankun.Wang
// Created Time    : 2024-12-15 22:08:15
// Last Modified   : 2024-12-22 19:32:20
#include <stdio.h>
#include <stdlib.h>

int main() {
    int size = 5;
    int *dynamicArray = (int *)malloc(size * sizeof(int));

    if (dynamicArray == NULL) {
        printf("Memory allocation failed.\n");
    }

    printf("Enter %d elements: ", size);
    for (int i=0; i<size; i++) {
        scanf("%d", &dynamicArray[i]);
    }

    printf("Dynamic Array: ");
    for (int i=0; i<size; i++) {
        printf("%d", dynamicArray[i]);
    }
    printf("\n");
    free(dynamicArray);
}
