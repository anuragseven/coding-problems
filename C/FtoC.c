#include<stdio.h>

int main()
{
    float f;
    printf("Enter temprature in Fahrenheit\n");
    scanf("%f",&f);

    float c=(f-32)*5/9;

    printf("The temprature in celsius is %.2f",c);


    return 0;
}