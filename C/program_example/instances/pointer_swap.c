// /usr/bin/gcc

// File Name       : pointer_swap.c
// Author          : Yuankun.Wang
// Created Time    : 2025-10-12 20:22:40
// Last Modified   : 2025-10-12 20:29:17
#include <stdio.h>

void cyclicSwap(int *a, int *b, int *c);

int main() {
    int a, b, c;
    printf("Input a, b, c: ");
    scanf("%d %d %d", &a, &b, &c);
    printf("before swap: \n");
    printf("a=%d\nb=%d\nc=%d\n", a, b, c);

    cyclicSwap(&a, &b, &c);

    printf("after swap: \n");
    printf("a=%d\nb=%d\nc=%d\n", a, b, c);
    return 0;
}

void cyclicSwap(int *a, int *b, int *c) {
    int temp;
    temp = *b;
    *b = *a;
    *a = *c;
    *c = temp;
}
