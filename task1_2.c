#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    printf("please enter a value\n");
    int n;
    scanf("%d",&n);
    printf("\noutput:\n");
    for(int i=n;i>0;i--)
    {
        printf("%d\n",i);
        sleep(1);
    }
    return 0;
}
