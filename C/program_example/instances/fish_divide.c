// /usr/bin/gcc

// File Name       : fish_divide.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-01 17:31:59
// Last Modified   : 2026-01-01 17:36:50
#include <stdio.h>

int main() {
    int n, j, k, l, m;
    for (n=5;;n++) {
        j = 4*(n-1)/5;
        k = 4*(j-1)/5;
        l = 4*(k-1)/5;
        m = 4*(l-1)/5;
        if (n%5==1 && j%5==1 && k%5==1 && l%5==1 && m%5==1) {
            printf("Total fishes: %d\n", n);
            printf("Every people see fished: %d %d %d %d\n", j, k, l, m);
            break;
        }
    }
    return 0;
}
