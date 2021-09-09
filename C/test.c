#include<stdio.h>

int main()

{   
     int a, b;
        char op;
        printf("Enter two numbers\n");

        scanf("%d %d", &a, &b);

        printf("Enter operator\n");
     
        scanf(" %c",&op);
        
         
         printf("op is %c",op);

        
        //printf("got numbers %d %d and operator  %c",a,b,op);


    return 0;
}