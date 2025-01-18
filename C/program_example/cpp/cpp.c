// /usr/bin/gcc

// File Name       : cpp.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-17 23:40:22
// Last Modified   : 2025-01-19 00:18:40
#include <stdio.h>

#define message_for(a, b) \
    printf(#a " and " #b ":We love you!\n")
#if !defined (MESSAGE)
    #define MESSAGE "You wish!"
#endif

#define MAX(x, y) ((x) > (y) ? (x) : (y))

int main(void)
{
//    printf("File: %s\n", __FILE__);
//    printf("Date: %s\n", __DATE__);
//    printf("Time: %s\n", __TIME__);
//    printf("Line: %s\n", __LINE__);
//    printf("ANSI: %s\n", __STDC__);
//    message_for(Carole, Debra);
    printf("Here is the message: %s\n", MESSAGE);
    printf("Max between 20 and 10 is %d\n", MAX(10, 20));
    return 0;
}
