// /usr/bin/gcc

// File Name       : error.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-21 23:34:02
// Last Modified   : 2025-01-21 23:47:04
#include <stdio.h>
#include <stdlib.h>

extern int errno;

int main()
{
    int dividend = 20;
    int divisor = 4;
    int quotient;
    if(divisor == 0)
    {
        fprintf(stderr, "divisor is 0 and exit...\n");
        exit(EXIT_FAILURE);
    }
    quotient = dividend / divisor;
    fprintf(stderr, "quotient value is: %d\n", quotient);
    exit(EXIT_SUCCESS);
}
