// /usr/bin/gcc

// File Name       : perfect_square.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-05 22:08:18
// Last Modified   : 2026-01-05 22:13:27
#include <stdio.h>

int main() {
    int i, j, m, n, x;
    for (i = 1; i < 168 / 2 + 1; i++) {
        if (168 % i == 0) {
            j = 168 / i;
            if (i > j && (i + j) % 2 == 0 && (i - j) % 2 == 0) {
                m = (i + j) / 2;
                n = (i - j) / 2;
                x = n * n - 100;
                printf("%d + 100 = %d * %d\n", x, n, n);
                printf("%d + 268 = %d * %d\n", x, m, m);
            }
        }
    }

    return 0;
}
