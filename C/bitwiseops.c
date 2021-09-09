#include<stdio.h>

int main()
{   
    // Binary Operators 
    // Bitwise OR |
    // Bitwise AND &
    // Bitwise XOR ^
    

    // a(60)  111100
    // b(13)  001101
    // OR     00111101  (61)
    // AND    00001100  (12)
    // XOR    00110001  (49)
    
    // Unary Operators
    // 1's complement ~
    // left shift  <<  (equivalent of multiplying by 2^k where k is no. of shifts)
    // Right shift >>  (equivalent of dividing by 2^k where k is no. of shifts)
    // a(60) 00111100
    // ~     11000011 (-61) (This is the binary representation of -61 i.e by taking 2's complement of 61 )
    // <<4   1111000000 (960) 
    // >>4   00000011  (3)
    
    int a=60;
    int b=13;
    
    printf("%d\n",a|b);
    printf("%d\n",a&b);
    printf("%d\n",a^b);
    printf("%d\n",~a);
    printf("%d\n",a<<4);
    printf("%d\n",a>>4);
    
    return 0;
}