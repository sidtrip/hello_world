#include <cs50.h>
#include <stdio.h>

int main (void)
{
    
    int x = get_int("X:");

    int y = get_int("Y:");

    if(x>y)
    { 
        printf("X is GREATER than Y\n");
    }
    else if(x<y)
    {
        printf("Y is GREATER than X\n");
    }
    else
    {
        printf("X=Y\n");
    }
}
