// /usr/bin/gcc

// File Name       : cpp.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-17 23:40:22
// Last Modified   : 2025-01-18 23:40:26
#include <stdio.h>

#define message_for(a, b) \
    printf(#a " and " #b ":We love you!\n")

int main()
{
//    printf("File: %s\n", __FILE__);
//    printf("Date: %s\n", __DATE__);
//    printf("Time: %s\n", __TIME__);
//    printf("Line: %s\n", __LINE__);
//    printf("ANSI: %s\n", __STDC__);
    message_for(Carole, Debra);
    return 0;
}
