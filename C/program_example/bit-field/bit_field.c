// /usr/bin/gcc

// File Name       : bit_field.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-10 23:29:45
// Last Modified   : 2025-01-11 23:10:48
#include <stdio.h>

struct packed_struct
{
    unsigned int f1 : 1;
    unsigned int f2 : 1;
    unsigned int f3 : 1;
    unsigned int f4 : 1;
    unsigned int type : 4;
    unsigned int my_int : 9;
};

int main()
{
    struct packed_struct pack;
    pack.f1 = 1;
    pack.f2 = 0;
    pack.f3 = 1;
    pack.f4 = 0;
    pack.type = 7;
    pack.my_int = 255;

    printf("f1: %u\n", pack.f1);
    printf("f2: %u\n", pack.f2);
    printf("f3: %u\n", pack.f3);
    printf("f4: %u\n", pack.f4);
    printf("type: %u\n", pack.type);
    printf("my_int: %u\n", pack.my_int);

    return 0;
}
