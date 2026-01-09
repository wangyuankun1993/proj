// /usr/bin/gcc

// File Name       : swap_number.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-09 22:17:27
// Last Modified   : 2026-01-09 22:25:00
#include <stdio.h>

int main() {
    int x, y, z, t;
    printf("Please input three number:");
    scanf("%d %d %d", &x, &y, &z);
    if (x > y) {
        t = x;
        x = y;
        y = t;
    }

    if (x > z) {
        t = x;
        x = z;
        z = t;
    }

    if (y > z) {
        t = y;
        y = z;
        z = t;
    }

    printf("Three number from little to big: %d, %d, %d", x, y, z);
}
