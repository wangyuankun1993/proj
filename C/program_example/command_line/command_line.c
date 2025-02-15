// /usr/bin/gcc

// File Name       : command_line.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-15 23:25:15
// Last Modified   : 2025-02-15 23:29:59
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Program name %s\n", argv[0]);

    if(argc == 2)
    {
        printf("The argument supplied is %s\n", argv[1]);
    }
    else if(argc > 2)
    {
        printf("Too many arguments supplied.\n");
    }
    else
    {
        printf("One argument expected.\n");
    }
}
