// /usr/bin/gcc

// File Name       : enum.c
// Author          : Yuankun.Wang
// Created Time    : 2024-12-22 23:42:48
// Last Modified   : 2025-01-01 20:06:33
#include <stdio.h>
#include <stdlib.h>

int main()
{
    enum color { red=1, green, blue };
    enum color favorite_color;
    printf("Please input your color: (1.red, 2.green, 3.blue):");
    scanf("%u", &favorite_color);

    switch(favorite_color)
    {
        case red:
            printf("Red");
            break;
        case green:
            printf("Green");
            break;
        case blue:
            printf("Blue");
            break;
        default:
            printf("Error");
    }

    return 0;
}
