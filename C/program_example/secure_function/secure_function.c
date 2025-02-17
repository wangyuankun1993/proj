// /usr/bin/gcc

// File Name       : secure_function.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-17 23:24:58
// Last Modified   : 2025-02-17 23:30:13
#include <stdio.h>
#include <string.h>

int main()
{
    char dest[20];
    const char *src = "Hello, World!";
    if (strcpy_s(dest, sizeof(dest), src) != 0)
    {
        printf("strcpy_s failed!\n");
        return 1;
    }
    else
    {
        printf("After strcpy_s: %s\n", dest);
    }
    const char *appendStr = "C Language";
    if (strcat_s(dest, sizeof(dest), appendStr) != 0)
    {
        printf("strcat_s failed!\n");
        return 1;
    }
    else
    {
        printf("After strcat_s: %s\n", dest);
    }
    return 0;
}
