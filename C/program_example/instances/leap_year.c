// /usr/bin/gcc

// File Name       : leap_year.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-06 22:42:51
// Last Modified   : 2026-01-07 22:35:16
#include <stdio.h>

int isLeapYear(int year) {
    if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)) {
        return 1;
    }
    return 0;
}

int main() {
    int year, month, day;
    int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int totalDays = 0;

    printf()
}
