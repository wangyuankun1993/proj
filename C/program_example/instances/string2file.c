// /usr/bin/gcc

// File Name       : string2file.c
// Author          : Yuankun.Wang
// Created Time    : 2025-12-21 22:27:39
// Last Modified   : 2025-12-21 22:41:44
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char sentence[1000];
    char c[1000];
    FILE *fptr;

    fptr = fopen("test.txt", "w");
    if(fptr == NULL)
    {
        printf("Error!");
        exit(1);
    }

    printf("Input string: \n");
    fgets(sentence, (sizeof sentence / sizeof sentence[0]), stdin);
    fprintf(fptr, "%s", sentence);
    fclose(fptr);

    fptr = fopen("test.txt", "r");
    if(fptr == NULL)
    {
        printf("Error opening file!");
        exit(1);
    }
    fscanf(fptr, "%[^\n]", c);
    printf("Reading content: \n%s", c);
    fclose(fptr);
}
