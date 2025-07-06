// /usr/bin/gcc

// File Name       : gcd.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 18:08:51
// Last Modified   : 2025-07-06 19:06:10
#include <stdio.h>

int main() {
    int n1, n2, i, gcd;
    printf("Please input two integers: ");
    scanf("%d %d", &n1, &n2);
    for (i=1; i<=n1 && i <= n2; ++i) {
        if (n1%i == 0 && n2%i == 0) {
            gcd = i;
        }
    }
    printf("%d and %d gcd is %d", n1, n2, gcd);
    return 0;
}
