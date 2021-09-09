#include <stdio.h>

int main()

{
    // Checks condition at the bottom of the loop
    // executes at least one

    int count = 0;
    int num = 0;

    //prints first 10 even numbers

    do
    {
        printf("%d\n", num);
        num += 2;
        count += 1;

    } while (count <10);

    return 0;
}