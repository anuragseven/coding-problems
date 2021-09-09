# include<stdio.h>

int main()
{
   /*
     *
     * *
     * * *
     * * * *

   */
    int rows;
    scanf("%d",&rows);

    {
        int i;
        for (i=0;i<rows;i++)
        {
            int j;
            for(j=0;j<=i;j++) printf("* ");
            printf("\n");
        }
    }

    return 0;
}