# include<stdio.h>

int main()

{

    unsigned  num;
    long long fact=1;

    printf("Enter a number\n");
    scanf("%u",&num);

    {
        int i;
        for (i=1;i<=num;i++) fact=fact*i;

    }
     printf("The factorial of %d  is %d",num,fact);

    return 0;
}