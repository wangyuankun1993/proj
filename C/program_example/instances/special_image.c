// /usr/bin/gcc

// File Name       : special_image.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-11 22:27:57
// Last Modified   : 2026-01-11 22:30:12
#include <stdio.h>

int main() {
    char a = 176, b = 219;
    printf("%c%c%c%c%c\n", b, a, a, a, b);
    printf("%c%c%c%c%c\n", a, b, a, b, a);
    printf("%c%c%c%c%c\n", a, a, b, a, a);
    printf("%c%c%c%c%c\n", a, b, a, b, a);
    printf("%c%c%c%c%c\n", b, a, a, a, b);
    return 0;
}
