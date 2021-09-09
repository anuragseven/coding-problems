// Format Specifiers

#include <stdio.h>

void main() {
    
    printf("print as decimal number %d\n",1);
    printf("print as decimal number at least 6 character wide%6d\n",7);
    printf("print as floating point %f\n",12.678);
    printf("print as floating point, 2 characters after decimal %.2f\n",12.3);
    printf("print as floating point at least 10 characters wide%10.0f\n",12.3);
    printf("print as ascii character %c\n",'a');
    printf("print as ascii character %c",97);
    return;
}