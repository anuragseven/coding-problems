# include<stdio.h>

int main()

{
    // c program which checks whether a number is prime
    int num;
    printf("Enter  a number\n");
    scanf("%d",&num);

    {
        int i;
        for (i=2;(i*i)<=num;i++)
        {
            if (num%i==0) 
            {
            printf("Not Prime");
            return 0;
            }
        }
    }
    
    printf("Prime");
    

    return 0;
}