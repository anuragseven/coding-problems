# include<stdio.h>

int main()
{ 
    // while(condition) statement;

    int i=0;

    while (++i<=10) printf("i= %d\n",i); 

    i=0;
    printf("\n");
    while (i++<=10) printf("i= %d\n",i);

    return 0;
}
/*
Output:
i= 1
i= 2
i= 3
i= 4
i= 5
i= 6
i= 7
i= 8
i= 9
i= 10

i= 1
i= 2
i= 3
i= 4
i= 5
i= 6
i= 7
i= 8
i= 9
i= 10
i= 11
*/