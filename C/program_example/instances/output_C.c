// /usr/bin/gcc

// File Name       : output_C.c
// Author          : Yuankun.Wang
// Created Time    : 2026-01-10 22:42:56
// Last Modified   : 2026-01-10 22:46:42
#include <stdio.h>

int main() {
    const char *c_pattern[] = {
        " ****",
        " *",
        " *",
        " ****"
    };

    printf("Print char C with *:\n");
    for (int i = 0; i < sizeof(c_pattern) / sizeof(c_pattern[0]); i++) {
        printf("%s\n", c_pattern[i]);
    }

    return 0;
}
