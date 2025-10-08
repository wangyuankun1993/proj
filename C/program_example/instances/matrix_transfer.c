// /usr/bin/gcc

// File Name       : matrix_transfer.c
// Author          : Yuankun.Wang
// Created Time    : 2025-10-08 22:09:40
// Last Modified   : 2025-10-08 22:37:57
#include <stdio.h>

int main() {
    int a[10][10], transpose[10][10], r, c, i, j;
    printf("Input matrix row and column: ");
    scanf("%d %d", &r, &c);
    printf("\nInput matrix element:\n");
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            printf("Input element a%d%d: ", i+1, j+1);
            scanf("%d", &a[i][j]);
        }

    printf("\ndisplay matrix: \n");
    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            printf("%d    ", a[i][j]);
            if (j == c-1) {
                printf("\n\n");
            }
        }

    for (i=0; i<r; ++i)
        for (j=0; j<c; ++j) {
            transpose[j][i] = a[i][j];
        }

    printf("\ndisplay transpose matrix:\n");
    for (i=0; i<c; ++i)
        for (j=0; j<r; ++j) {
            printf("%d    ", transpose[i][j]);
            if (j == r-1) {
                printf("\n\n");
            }
        }
    return 0;
}
