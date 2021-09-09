#include<stdio.h>

int main()
{
   
    // string constant is represented as "string"
    
    printf("anurag tripathi\n");

    // In C string are arrays of characters

    char s[]="a string";
    printf("%s\n",s);

    // a string always ends with a null string \0

    int l=0;
   
    while (s[l]!='\0') l+=1;
    
    printf("The length of string s is %d",l); 

    return 0;
}