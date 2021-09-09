# include<stdio.h>

int main()
{
    // continue forces next iteration of the loop

    // read 10 integers from user and sum only positive integers

    {
        int i,sum=0;
        for (i=0;i<10;i++)
        {

            int num;
            scanf("%d",&num);
            if (num<0) continue;

            sum+=num;
        }

        printf("The sum is %d",sum);
    }


    return 0;
}