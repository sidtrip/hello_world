#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int n;
    do
    {
        n = get_int("enter number of rows and columns?\n");
    }
    while(n<1);
    
    for(int i=0;i<n;i++)
    {
    
        for(int j=0;j<n;j++)
        {
            printf("#$");
        }
    printf("\n");

    }
}