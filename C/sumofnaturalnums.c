# include<stdio.h>

int main()
{  int n;
   printf("Enter n , to get sum of first n natural numbers\n");
   scanf("%d",&n);

   {
       int i;
       int sum=0;
       for(i=1;i<=n;i++) sum+=i;

       printf("Sum of first n natural number is %d",sum);
   }

    return 0;
}