#include <stdio.h>

void func1(void);

static int count=10;

int main() {
    while (count--) {
        func1();
    }
    return 0;
}

void func1(void) {
    static int thingy=5;
    thingy++;
    printf("thingy is %d, count is %d\n", thingy, count);
}
