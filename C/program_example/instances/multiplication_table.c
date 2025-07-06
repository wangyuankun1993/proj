// /usr/bin/gcc

// File Name       : multiplication_table.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 17:49:03
// Last Modified   : 2025-07-06 17:54:17
#include <stdio.h>

int main() {
    int i, j;
    for (i=1; i<=9; i++) {
        for (j=1; j<=i; j++) {
            printf("%d x %d = %d\t", i, j, i*j);
        }
        printf("\n");
    }
    return 0;
}
