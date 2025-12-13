// /usr/bin/gcc

// File Name       : struct.c
// Author          : Yuankun.Wang
// Created Time    : 2025-12-06 09:51:58
// Last Modified   : 2025-12-13 22:26:00
#include <stdio.h>
struct student
{
    char name[50];
    int roll;
    float marks;
} s;

int main()
{
    printf("Input info: \n");
    
    printf("Name: ");
    scanf("%s", &s.name);

    printf("Number: ");
    scanf("%d", &s.roll);

    printf("Mark: ");
    scanf("%f", &s.marks);

    printf("Display info: \n");
    printf("Name: %s\n", s.name);
    printf("Number: %d\n", s.roll);
    printf("Mark: %.1f\n", s.marks);

    return 0;
}
