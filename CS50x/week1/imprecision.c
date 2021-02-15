#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float x = get_float("enter a value for x: ");
    float y = get_float("enter y value: ");

    printf("the value of x by y is %.50f", x/y);
    printf("\n");
}
