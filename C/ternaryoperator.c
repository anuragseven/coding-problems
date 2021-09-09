#include<stdio.h>

int main()
{
    
   // cond ?: st1:st2 
   // if cond is true st1 will run otherwise st2 will run.

   int a=20;
   int b=16;

   a<b ?printf("%d is smaller than %d",a,b):printf("%d is greater than %d",a,b);

    return 0;
}