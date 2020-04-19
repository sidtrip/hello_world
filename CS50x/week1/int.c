#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int age = get_int("What's your age?\n");
    int days = age * 365;
    printf("Ÿou are at least %i days old. \n", days);

//This can be also be Written as:

    printf("You are at least %i days old. \n", get_int("What's your age?\n")*365);


}
