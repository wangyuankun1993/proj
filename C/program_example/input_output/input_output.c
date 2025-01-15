// /usr/bin/gcc

// File Name       : input_output.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-13 23:44:37
// Last Modified   : 2025-01-15 23:41:55
#include <stdio.h>

int main()
{
    FILE *file;
    file = fopen("example.txt", "w");
    if (file != NULL)
    {
        fprintf(file, "Hello, world!\n");
        fclose(file);
    }

    char buffer[100];
    file = fopen("example.txt", "r");
    if (file != NULL)
    {
        fscanf(file, "%s", buffer);
        printf("Read from file: %s\n", buffer);
        fclose(file);
    }
    return 0;
}
