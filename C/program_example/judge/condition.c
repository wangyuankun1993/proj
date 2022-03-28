#include <stdio.h>

int main() {
    int num;
    printf("Input a number: ");
    scanf("%d", &num);
    (num % 2 == 0)?printf("even"):printf("odd");
    printf("\n");
}
