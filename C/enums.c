#include<stdio.h>

int main()
{
    // enum keyword is used to define enumeration constants

    enum boolean {NO,YES};

    // by default No has value 0 and YES has 1 , futher elements will have value 2, 3 and so on

    printf("%d\n",NO);
    printf("%d",YES);

    return 0;
}