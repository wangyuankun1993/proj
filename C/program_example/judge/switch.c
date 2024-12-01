#include <stdio.h>

int main() {
    char grade = 'B';

    switch (grade) {
        case 'A':
            printf("Excellent!\n");
            break;
        case 'B':
        case 'C':
            printf("Well done!\n");
            break;
        case 'D':
            printf("Pass!\n");
            break;
        case 'F':
            printf("Try more!\n");
            break;
        default:
            printf("Invalid!\n");
    }
    printf("Your grade is: %c\n", grade);

    return 0;
}
