// /usr/bin/gcc

// File Name       : __FILE__.c
// Author          : Yuankun.Wang
// Created Time    : 2025-12-21 22:47:22
// Last Modified   : 2025-12-21 22:49:14
#include <stdio.h>
int main()
{
    FILE *fp;
    char c;
    fp = fopen(__FILE__, "r");
    do {
        c = getc(fp);
        putchar(c);
    } while(c != EOF);
    fclose(fp);
    return 0;
}
