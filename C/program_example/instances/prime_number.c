// /usr/bin/gcc

// File Name       : prime_number.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-17 21:34:57
// Last Modified   : 2026-01-17 21:47:02
#include <stdio.h>

int main() {
    int i, j;
    int count = 0;
    for (i = 101; i <= 200; i++) {
        for (j = 2; j < i; j++) {
            if (i % j == 0) {
                break;
            }
        }
        if (j >= i) {
            printf("%d ", i);
            count++;
            if (count % 5 == 0) {
                printf("\n");
            }
        }
    }
    return 0;
}
