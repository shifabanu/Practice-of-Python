// TASK:  Write a C++ code that will swap two values. The value can either
// be an integer or string. Create a base class and sub class for each value
// type. The code shall have a main function. You have 6 minutes to complete.
#include<stdio.h>

class B
{
}

class C
{
}

class A : B
{
	C mycinst;
  void swap(int *x, int *y)
{
  int tmp = *x;
  *x= *y;
  *y = tmp;
  return;
}
}


main()
{
	int a=10, b=9;
    A.swap(&a,&b);
  	printf("The nos. are a=%d and b=%d", a, b);
    
  
}
