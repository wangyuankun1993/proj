// /usr/bin/gcc

// File Name       : union.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-09 23:12:59
// Last Modified   : 2025-01-09 23:28:52
#include <stdio.h>
#include <string.h>

union Data
{
    int i;
    float f;
    char str[20];
};

int main()
{
    union Data data;

    data.i = 10;
    printf("data.i: %d\n", data.i);

    data.f = 22.5;
    printf("data.f: %f\n", data.f);

    strcpy(data.str, "C Programming");
    printf("data.str: %s\n", data.str);
    return 0;
}
