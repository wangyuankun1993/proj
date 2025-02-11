// /usr/bin/gcc

// File Name       : memory_manage.c
// Author          : Yuankun.Wang
// Created Time    : 2025-02-11 23:06:59
// Last Modified   : 2025-02-11 23:18:33
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char name[100];
    char *description;

    strcpy(name, "Zara Ali");

    description = (char *)malloc( 30 * sizeof(char));
    if (description == NULL)
    {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }
    else
    {
        strcpy(description, "Zara ali a DPS student");
    }
    description = (char *)realloc( description, 100 * sizeof(char));
    if (description == NULL)
    {
        fprintf(stderr, "Error - unable to allocate required memory\n");
    }
    else
    {
        strcat(description, "She is in class 10th");
    }
    printf("Name = %s\n", name);
    printf("Description: %s\n", description);
    free(description);
}
