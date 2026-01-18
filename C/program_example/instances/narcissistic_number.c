// /usr/bin/gcc

// File Name       : narcissistic_number.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-18 22:43:20
// Last Modified   : 2026-01-18 22:50:14
#include <stdio.h>

int main() {
    int i, x, y, z, sum;
    for (i = 100; i < 1000; i++) {
        x = i % 10; // the unit
        y = (i / 10) % 10; // decade
        z = (i / 100) % 10; // hundred
        sum = x * x * x + y * y * y + z * z * z;
        if (i == sum) {
            printf("%d\n", i);
        }
    }
    return 0;
}
