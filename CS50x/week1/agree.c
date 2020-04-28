#include <cs50.h>
#include <stdio.h>

int main (void)
{
    
    char c = get_char("Do you agree?");

    if (c=='y' || c=='Y')
    {
        printf("You have agreed! Yay!\n");
    }
    else if (c=='n'|| c=='N')
    {
        printf("why didn't you agree\n");
    }

}
