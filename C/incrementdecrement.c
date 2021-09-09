#include<stdio.h>

int main()
{

    // preincrement ++n , increment n before its value is used
    int n=10;
    int i=++n;
    printf("i is %d and n is %d\n",i,n); // i is 11 and n is 11
  
    // postincrement n++ , increment n after its value is used
    int j=n++;
    printf("j is %d and n is %d\n",j,n); // j is 11 and n is 12

    // predecrement --n, decrement n before its value is used

    int l =--n;
    
    printf("l is %d and n is %d\n",l,n); // l is 11 and n is 11

    // postdecrement --n, decrement n before its value is used

    int m=n--;

    printf("m is %d and n is %d\n",m,n); // m is 11 and n is 10



    return 0;


}