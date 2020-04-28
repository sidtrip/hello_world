#include <stdio.h>
#include <cs50.h>
#include <unistd.h>

int main(void)
{
    int n= get_int("");

    switch(n)
    {

        case 1:
            printf("One\n");
            break;
        case 2:
            printf("Two\n");
            break;
        case 3:
            printf("Three\n");
            break;
        case 4:
            printf("Four\n");
            break;
        case 5:
            printf("Five\n");
            break;
        default:
            printf("Sorry man\n");    

    }

    switch(n)
    {
        case 5:
            printf("Five, \n");
            sleep(1);
        case 4:
            printf("Four, \n");
            sleep(1);
        case 3:
            printf("Three, \n");
            sleep(1);
        case 2:
            printf("Two, \n");
            sleep(1);
        case 1:
            printf("One, \n");
            sleep(1);
        default:
            printf("Blast-Off!\n");
            sleep(1);
    }

}
