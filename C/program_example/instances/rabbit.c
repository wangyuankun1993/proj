// /usr/bin/gcc

// File Name       : rabbit.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-14 22:05:19
// Last Modified   : 2026-01-14 22:14:57
#include <stdio.h>

int main() {
    int a = 1, b = 1, temp, i;
    printf("%12d%12d", a, b); // first, second

    for (i = 3; i <= 20; i += 2) {
        temp = a + b;
        printf("%12d", temp); // third
        a = b;
        b = temp;
        temp = a + b;
        printf("%12d\n", temp); // fourth
        a = b;
        b = temp;
    }
    return 0;
}
