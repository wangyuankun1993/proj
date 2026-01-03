// /usr/bin/gcc

// File Name       : bonus.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-03 22:52:58
// Last Modified   : 2026-01-03 23:29:21
#include <stdio.h>

int main() {
    double profit;
    double bonus10, bonus20, bonus40, bonus60, bonus100, bonus;
    printf("Please input profit: ");
    scanf("%lf", &profit);
    bonus10 = 100000 * 0.1;
    bonus20 = bonus10 + 100000 * 0.075;
    bonus40 = bonus20 + 200000 * 0.05;
    bonus60 = bonus40 + 200000 * 0.03;
    bonus100 = bonus60 + 400000 * 0.015;
    if (profit <= 100000) {
        bonus = profit * 0.1;
    } else if (profit <= 200000) {
        bonus = bonus10 + (profit - 100000) * 0.075;
    } else if (profit <= 400000) {
        bonus = bonus20 + (profit - 200000) * 0.05;
    } else if (profit <= 600000) {
        bonus = bonus40 + (profit - 400000) * 0.03;
    } else if (profit <= 1000000) {
        bonus = bonus60 + (profit - 600000) * 0.015;
    } else {
        bonus = bonus100 + (profit - 1000000) * 0.01;
    }
    printf("The total bonus is %lf.\n", bonus);

    return 0;
}
