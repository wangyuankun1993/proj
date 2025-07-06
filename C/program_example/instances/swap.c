// /usr/bin/gcc

// File Name       : swap.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 16:29:18
// Last Modified   : 2025-07-06 16:34:07
#include <stdio.h>

int main() {
    double firstNumber, secondNumber, temporaryVariable;

    printf("Please input first number: ");
    scanf("%lf", &firstNumber);

    printf("Please input second number: ");
    scanf("%lf", &secondNumber);

    temporaryVariable = firstNumber;
    firstNumber = secondNumber;
    secondNumber = temporaryVariable;

    printf("\nAfter swap, the first number is: %.2lf\n", firstNumber);
    printf("\nAfter swap, the second number is: %.2lf\n", secondNumber);

    return 0;
}
