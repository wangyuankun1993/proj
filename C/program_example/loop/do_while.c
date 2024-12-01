// /usr/bin/gcc

// File Name       : do_while.c
// Author          : Yuankun.Wang
// Created Time    : 2024-12-01 18:26:43
// Last Modified   : 2024-12-01 18:28:09
#include <stdio.h>

int main() {
    int a = 10;
    do {
        printf("a value is: %d\n", a); 
        a++;
    } while(a < 20);

    return 0;
}
