# include<stdio.h>

int main()
{ 
    // Evaluation depends upon two things : 1) Precedence 2) Order of Associativity
    // if operators have same precedence then we use associativity to decide which 
    // operation to carry out first

    int a = 5*3-4/2*2+1;
    printf("a= %d\n",a); // a= 12
   
    int b=2+a++;
    printf("b= %d\n",b); // b= 14

    int c=++a+6;
    printf("c= %d",c); // c= 20
    return 0;
}