// /usr/bin/gcc

// File Name       : integer_add.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 11:15:14
// Last Modified   : 2025-07-06 11:26:22
#include <stdio.h>
int main() {
    int firstNumber, secondNumber, sumOfTwoNumber;
    printf("Please input two integers: ");
    scanf("%d %d", &firstNumber, &secondNumber);
    sumOfTwoNumber = firstNumber + secondNumber;
    printf("%d + %d = %d\n", firstNumber, secondNumber, sumOfTwoNumber);
    return 0;
}
