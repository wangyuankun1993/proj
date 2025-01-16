// /usr/bin/gcc

// File Name       : input_output.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-13 23:44:37
// Last Modified   : 2025-01-16 23:02:58
#include <stdio.h>

int main()
{
    FILE *fp = NULL;
    fp = fopen("/home/wangyuankun/proj/C/program_example/input_output/test.txt", "w+");
    fprintf(fp, "This is testing for fprintf...\n");
    fputs("This is testing for fputs...\n", fp);
    fclose(fp);
}
