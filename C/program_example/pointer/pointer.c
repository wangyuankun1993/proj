#include <stdio.h>

int main() {
    int var = 20;
    int *ip;
    ip = &var;
    printf("var address: %p\n", &var);
    printf("ip saved address: %p\n", ip);
    printf("ip value: %d\n", *ip);
    return 0;
}
