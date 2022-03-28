#include <stdio.h>

int main()
{
    int a = 21;
    int b = 10;
    int c;

    c = a + b;
    printf("Line 1-c value: %d\n", c);
    c = a - b;
    printf("Line 2-c value: %d\n", c);
    c = a * b;
    printf("Line 3-c value: %d\n", c);
    c = a / b;
    printf("Line 4-c value: %d\n", c);
    c = a % b;
    printf("Line 5-c value: %d\n", c);

    printf("First assignment and then operation：\n");
    c = a++; // First assignment and then add 1, c is 21, a is 22
    printf("Line 6-c value: %d, 1-a value: %d\n", c, a);
    c = a--; // First assignment and then subtract 1, c is 22, a is 21
    printf("Line 7-c value: %d, 2-a value: %d\n", c, a);

    printf("First operation and then assignment：\n");
    a = 10;
    c = ++a;
    printf("Line 8-c value: %d, 3-a value: %d\n", c, a);
    c = --a;
    printf("Line 9-c value: %d, 4-a value: %d\n", c, a);

    if (a == b) {
        printf("Line 5 - a=b\n");
    }
    else {
        printf("Line 5 - a!=b\n");
    }

    if (a && b) {
        printf("Line 6 - Condition is True.\n");
    }
    if (a || b) {
        printf("Line 7 - Condition is True.\n");
    }


}
