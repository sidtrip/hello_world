//program prints out two mario pyramids of height specified by user
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Enter Height of the pyramid: \n");
    }
    while (h < 1 || h > 8);
//do while loop so that unless our value is between 1 and 8 included we keep asking    
    for (int i = 0; i < h; i++)     //Loop for rows specified by user as h
    {
        for (int j = 0 ; j < h - i - 1; j++)    //Loop for decreasing no of spaces per row
        {
            printf(" ");
        }   
        for (int j = 0; j < i + 1; j++)     //Loop for ircreasing no of hashes per row
        {
            printf("#");
        }   
        printf("  ");   //two space distance between pyramids
        
        for (int j = 0; j < i + 1; j++)     //loop for right half of pyramid
        {
            printf("#");
        }    
        printf("\n");
    }
}
