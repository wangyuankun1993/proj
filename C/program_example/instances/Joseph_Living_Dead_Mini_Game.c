// /usr/bin/gcc

// File Name       : Joseph_Living_Dead_Mini_Game.c
// Author          : Yuankun.Wang
// Created Time    : 2025-12-28 21:36:54
// Last Modified   : 2025-12-28 22:07:07
#include <stdio.h>

int c = 0;
int i = 1;
int j = 0;
int a[30] = {0};
int b[30] = {0};

int main() {
    while (i <= 31) {
        if (i == 31) {
            i = 1;
        } else if (c == 15) {
            break;
        } else {
            if (b[i] != 0) {
                i++;
                continue;
            } else {
                j++;
                if (j != 9) {
                    i++;
                    continue;
                } else {
                    b[i] = 1;
                    a[i] = j;
                    j = 0;
                    printf("The %d number get off.\n", i);
                    i++;
                    c++;
                }
            }
        }
    }
}
