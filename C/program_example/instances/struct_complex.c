// /usr/bin/gcc

// File Name       : struct_complex.c
// Author          : Yuankun.Wang
// Created Time    : 2025-12-17 22:44:40
// Last Modified   : 2025-12-17 22:59:08
#include <stdio.h>

typedef struct complex
{
    float real;
    float imag;
} complex;

complex add(complex n1, complex n2);

int main()
{
    complex n1, n2, temp;
    printf("First complex \n");
    printf("Input real and imag:\n");
    scanf("%f %f", &n1.real, &n1.imag);

    printf("Second complex \n");
    printf("Input real and imag:\n");
    scanf("%f %f", &n2.real, &n2.imag);

    temp = add(n1, n2);
    printf("Sum = %.1f + %.1f", temp.real, temp.imag);

    return 0;
}

complex add(complex n1, complex n2)
{
    complex temp;
    temp.real = n1.real + n2.real;
    temp.imag = n1.imag + n2.imag;

    return(temp);
}
