// /usr/bin/gcc

// File Name       : enum.c
// Author          : Yuankun.Wang
// Created Time    : 2024-12-22 23:42:48
// Last Modified   : 2024-12-22 23:50:46
#include <stdio.h>

enum DAY
{
    MON=1, TUE, WED, THU, FRI, SAT, SUN
};

int main() {
    enum DAY day;
    day = WED;
    printf("%d", day);
    return 0;
}
