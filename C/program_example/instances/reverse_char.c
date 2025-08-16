// /usr/bin/gcc

// File Name       : reverse_char.c
// Author          : Yuankun.Wang
// Created Time    : 2025-08-16 18:18:26
// Last Modified   : 2025-08-16 18:29:01
#include <stdio.h>

void reverseSentence();

int main() {
    printf("Input a string: ");
    reverseSentence();

    return 0;
}

void reverseSentence() {
    char c;
    scanf("%c", &c);
    if(c != '\n') {
        reverseSentence();
        printf("%c", c);
    }
}
