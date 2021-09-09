#include<stdio.h>

int main()
{
    // constant value that are present in an expression can cause the type conversion
    // 40 will be converted to long
    int a=2+5+40l;
    printf("%d",a);


    // use const to make variables constant 

    const float pi=3.14;
    
    // wil cause error:
    //pi=4.44;

    return 0;
}