// /usr/bin/gcc

// File Name       : pointer.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-01 21:28:08
// Last Modified   : 2025-01-02 23:51:12
#include <stdio.h>

int main()
{
    char str[] = "Hello";
    char *ptr = &str[4];
    printf("initial: %c\n", *ptr);
    ptr--;
    printf("initial: %c\n", *ptr);
    return 0;

}
