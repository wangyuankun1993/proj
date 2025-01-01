// /usr/bin/gcc

// File Name       : pointer.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-01 21:28:08
// Last Modified   : 2025-01-01 22:53:16
#include <stdio.h>

int main()
{
    int var = 10;
    int *ptr = NULL;
    int *ip;
    ip = &var;
    printf("var address: %p\n", &var);
    printf("ip storage address: %p\n", ip);
    printf("pointer access value: %d\n", *ip);
    printf("ptr address: %p\n", ptr);
    printf("ptr access value: %d\n", *ptr);

    return 0;
}
