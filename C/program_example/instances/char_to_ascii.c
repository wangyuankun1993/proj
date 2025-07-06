// /usr/bin/gcc

// File Name       : char_to_ascii.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 11:40:41
// Last Modified   : 2025-07-06 11:51:23
#include <stdio.h>
int main() {
    char c;
    printf("Please input char: ");
    scanf("%c", &c);
    printf("%c acsii is %d", c, c);
    return 0;
}
