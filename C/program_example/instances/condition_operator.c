// /usr/bin/gcc

// File Name       : condition_operator.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-20 22:28:44
// Last Modified   : 2026-01-20 22:31:47
#include <stdio.h>

int main() {
    int score;
    char grade;
    printf("Please input score: ");
    scanf("%d", &score);
    grade = (score >= 90) ? 'A' : ((score >= 60) ? 'B' : 'C');
    printf("%c\n", grade);
    return 0;
}
