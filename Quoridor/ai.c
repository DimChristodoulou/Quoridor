#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int a;
	srand(time(NULL));
	a=rand()%10+1;
	printf("%d",a);
}
