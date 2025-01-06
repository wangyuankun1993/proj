// /usr/bin/gcc

// File Name       : string.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-05 23:29:16
// Last Modified   : 2025-01-05 23:41:51
#include <stdio.h>
#include <string.h>

int main()
{
    char str1[14] = "runoob";
    char str2[14] = "google";
    char str3[14];
    int len;
    strcpy(str3, str1);
    printf("strcpy(str3, str1): %s\n", str3);
    strcat(str1, str2);
    printf("strcat(str1, str2): %s\n", str1);
    len = strlen(str1);
    printf("strlen(str1): %d\n", len);
    return 0;
}
