#include <stdio.h>

int main()
{
    // for(initialisation;condition;increment) statement;
    {
        //new block 
        // enable c99 to use initial declarations
        int i;
        for (i = 0; i <= 10; ++i)
        {
            printf("i= %d\n", i);
        }
    }


    return 0;
}