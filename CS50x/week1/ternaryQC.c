#include <stdio.h>
#include <cs50.h>
#include <unistd.h>

int main(void)
{
    int n= get_int("");

    int x = (n<5)? 1 : 9;

    printf("x= %i",x);
}
