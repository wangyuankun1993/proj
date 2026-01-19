// /usr/bin/gcc

// File Name       : prime_factor.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-19 22:46:00
// Last Modified   : 2026-01-19 22:49:41
#include <stdio.h>

int main() {
    int n, i;
    printf("Please input number:");
    scanf("%d", &n);
    printf("%d=", n);
    for (i = 2; i <= n; i++) {
        while (n % i == 0) {
            printf("%d", i);
            n /= i;
            if (n != 1) {
                printf("*");
            }
        }
    }
    printf("\n");
    return 0;
}
