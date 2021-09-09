#include <stdio.h>

int main()
{
    // switch is multiple branch selection statement

    // a simple calculator

    while (1)
    {
        double a, b;
        char op;
        printf("Enter two numbers\n");

        scanf(" %lf %lf", &a, &b);

       
        printf("Enter operator\n");
     
        scanf(" %c",&op);

        switch (op)
        {
        case '+':
            printf("Sum of %.2lf and %.2lf is %.2f \n", a, b, a + b);
            break;
        case '-':
            printf("Difference of %.2lf and %.2lf is %.2lf \n", a, b, a - b);
            break;

        case '*':
            printf("Multiplication of %.2lf and %.2lf is %.2lf \n", a, b, a * b);
            break;

        case '/':
            printf("Division of %.2lf and %.2lf is %.2lf \n", a, b, a / b);
            break;
        default:
            printf("Enter valid operator\n");
            break;
        }
    }
    return 0;
}