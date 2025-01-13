// /usr/bin/gcc

// File Name       : input_output.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-13 23:44:37
// Last Modified   : 2025-01-13 23:53:29
#include <stdio.h>

int main()
{
    int c;
    printf("Enter a value: ");
    c = getchar();
    printf("\nYou entered: ");
    putchar(c);
    printf("\n");
    return 0;
}
