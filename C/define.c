#include<stdio.h>
# define X 30
int main()
{   
    // #define is used to define some values with a name (string), this defined string is known as Macro definition in C, 
    // C++ while const is a keyword or used to make the value of an identifier (that is constant) constant.

    // #define is not scope controlled whereas const is scope controlled
    
    // Macros (#define) can be redefined but const cannot
    
    printf("%d",X);
    return 0;
}