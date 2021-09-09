# include<stdio.h>

int main()
{   
    // short and long are used with int and double 
    //  don't need to specify int .
    short i;  // 2 bytes
    long j;   // 4 bytes 
    long long k;  // 8 bytes
    long double d; // 16 bytes

    printf("%d\n",sizeof(i));
    printf("%d\n",sizeof(j));
    printf("%d\n",sizeof(k));
    printf("%d\n",sizeof(d));
  

    // signed and unsigned are used with characters and integers
    // unsigned integers contain only zero or positive integers
    // use %u for format specifier
    unsigned  l;
    l=-1;  //  converted to unsigned by adding  UINT_MAX + 1 
    printf("%u",l); // 4294967295
    return 0;
}