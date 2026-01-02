// /usr/bin/gcc

// File Name       : digital_combination.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-02 23:24:26
// Last Modified   : 2026-01-02 23:27:33
#include <stdio.h>

int main() {
    int i, j, k;
    printf("\n");
    for (i=1; i<5; i++) {
        for (j=1; j<5; j++) {
            for (k=1; k<5; k++) {
                if (i != k && i != j && j != k) {
                    printf("%d, %d, %d\n", i, j, k);
                }
            }
        }
    }

    return 0;
}
