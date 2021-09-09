#include<stdio.h>

int main()
{   
    // during some operation type conversion can take place if operators are of different type
    int a=10;
    float b=25.02;

    printf("%f\n",a+b); // 35.020000 , a is converted to float type

    // type conversion can result in loss of data

    a=b;
    printf("%d",a);  // 25
    
    return 0;
}