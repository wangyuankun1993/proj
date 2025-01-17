// /usr/bin/gcc

// File Name       : input_output.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-13 23:44:37
// Last Modified   : 2025-01-17 23:28:50
#include <stdio.h>

int main()
{
    FILE *fp = NULL;
    char buff[255];

    fp = fopen("/home/wangyuankun/proj/C/program_example/input_output/test.txt", "r");
    fscanf(fp, "%s", buff);
    printf("1: %s\n", buff);

    fgets(buff, 255, (FILE*)fp);
    printf("2: %s\n", buff);

    fgets(buff, 255, (FILE*)fp);
    printf("3: %s\n", buff);
    fclose(fp);
}
