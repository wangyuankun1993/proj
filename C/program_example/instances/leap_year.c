// /usr/bin/gcc

// File Name       : leap_year.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-06 22:42:51
// Last Modified   : 2026-01-08 22:29:43
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

    printf("Please input year, month, day(format: year month day):");
    scanf("%d %d %d", &year, &month, &day);

    if (isLeapYear(year)) {
        daysInMonth[1] = 29;
    }

    for (int i = 0; i < month - 1; i++) {
        totalDays += daysInMonth[i];
    }
    totalDays += day;
    printf("%d year %d month %d day is the %dth day of the year.\n", year, month, day, totalDays);

    return 0;
}
