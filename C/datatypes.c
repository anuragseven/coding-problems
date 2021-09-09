#include <stdio.h>

int main()
{
    char c; // char data type size 1 byte
    int i; // int data type 2 or 4 bytes (depends upon machine )
    float f; // single precision floating point data type 4 bytes
    double d; // double precision floating point 8 bytes 

    // sizeof operator which returns the size of data types and variables

    printf("%d\n",sizeof(c));
    printf("%d\n",sizeof(i));
    printf("%d\n",sizeof(f));
    printf("%d",sizeof(d));

    return 0;
}