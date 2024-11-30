#include <stdio.h>

int main()
{
//    int a = 21;
//    int b = 10;
//    int c;
//
//    c = a + b;
//    printf("Line 1-c value: %d\n", c);
//    c = a - b;
//    printf("Line 2-c value: %d\n", c);
//    c = a * b;
//    printf("Line 3-c value: %d\n", c);
//    c = a / b;
//    printf("Line 4-c value: %d\n", c);
//    c = a % b;
//    printf("Line 5-c value: %d\n", c);
//
//    printf("First assignment and then operation：\n");
//    c = a++; // First assignment and then add 1, c is 21, a is 22
//    printf("Line 6-c value: %d, 1-a value: %d\n", c, a);
//    c = a--; // First assignment and then subtract 1, c is 22, a is 21
//    printf("Line 7-c value: %d, 2-a value: %d\n", c, a);
//
//    printf("First operation and then assignment：\n");
//    a = 10;
//    c = ++a;
//    printf("Line 8-c value: %d, 3-a value: %d\n", c, a);
//    c = --a;
//    printf("Line 9-c value: %d, 4-a value: %d\n", c, a);
//
//    if (a == b) {
//        printf("Line 10 - a=b\n");
//    }
//    else {
//        printf("Line 11 - a!=b\n");
//    }
//
//    if (a && b) {
//        printf("Line 12 - Condition is True.\n");
//    }
//    if (a || b) {
//        printf("Line 13 - Condition is True.\n");
//    }

//    unsigned int a = 60;
//    unsigned int b = 13;
//    int c;
//    c = a & b;
//    printf("Line 14 - c value is: %d\n", c);
//
//    c = a | b;
//    printf("Line 15 - c value is: %d\n", c);
//
//    c = a ^ b;
//    printf("Line 16 - c value is: %d\n", c);
//
//    c = ~a;
//    printf("Line 17 - c value is: %d\n", c);
//
//    c = a << 2;
//    printf("Line 18 - c value is: %d\n", c);
//
//    c = a >> 2;
//    printf("Line 19 - c value is: %d\n", c);

    int a = 4;
    short b;
    double c;
    int* ptr;

    /* sizeof */
    printf("Line 20 - a size is: %lu\n", sizeof(a));
    printf("Line 21 - b size is: %lu\n", sizeof(b));
    printf("Line 22 - c size is: %lu\n", sizeof(c));

    /* & and * */
    ptr = &a;
    printf("a value is: %d\n", a);
    printf("*ptr value is: %d\n", *ptr);

    /* condition */
    a = 10;
    b = (a == 1) ? 20 : 30;
    printf("b value is: %d\n", b);
}
