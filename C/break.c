# include<stdio.h>

int main()
{
    // break terminates the loop

    // read integers until a negative one is encountered or the count reaches 10
    int count=0;
    int sum=0;
    while (count<10)
    {   int num;
        scanf("%d",&num);
        if (num<0) break;
        sum+=num;
        count+=1;
    }
    printf("The sum is %d",sum);
    return 0;
}
