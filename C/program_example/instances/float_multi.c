// /usr/bin/gcc

// File Name       : float_multi.c
// Author          : Yuankun.Wang
// Created Time    : 2025-07-06 11:27:26
// Last Modified   : 2025-07-06 11:30:09
#include <stdio.h>
int main() {
    float num1, num2, product;
    printf("Please input two float: ");
    scanf("%f %f", &num1, &num2);
    product = num1 * num2;
    printf("%.2f multi %.2f equal %.2f\n", num1, num2, product);
    return 0;
}
