#include <cs50.h>
#include <stdio.h>

void cough(int n);

int main(void)
{
    for(int i=0;i<3;i++)
{
    cough(4);
}
}




void cough (int n)
{
    for(int i=0;i<=n;i++)
    {
        printf("Cough\n");
    }
}
