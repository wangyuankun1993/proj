// /usr/bin/gcc

// File Name       : matrix_add.c
// Author          : Yuankun.Wang
// Created Time    : 2025-10-08 19:06:40
// Last Modified   : 2025-10-08 19:23:32
#include <stdio.h>

int main() {
    int r, c, a[100][100], b[100][100], sum[100][100], i, j;
    printf("Input row(1~100): ");
    scanf("%d", &r);
    printf("Input column(1~100): ");
    scanf("%d", &c);
    printf("\nInput first matrix elements:\n");
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            printf("Input element a%d%d: ", i+1, j+1);
            scanf("%d", &a[i][j]);
        }

    printf("\nInput second matrix elements:\n");
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            printf("Input element b%d%d: ", i+1, j+1);
            scanf("%d", &b[i][j]);
        }

    // add
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            sum[i][j] = a[i][j] + b[i][j];
        }

    // result
    printf("\nadd result is: \n\n");
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            printf("%d    ", sum[i][j]);
            if (j == c-1) {
                printf("\n\n");
            }
        }

    return 0;
}
