// /usr/bin/gcc

// File Name       : divide.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 15:40:03
// Last Modified   : 2025-07-06 16:12:27
#include <stdio.h>

int main() {
    int dividend, divisor, quotient, remainder;
    printf("Please input dividend: ");
    scanf("%d", &dividend);

    printf("Please input divisor: ");
    scanf("%d", &divisor);

    quotient = dividend / divisor;

    remainder = dividend % divisor;

    printf("quotient = %d\n", quotient);
    printf("remainder = %d\n", remainder);

    return 0;
}
