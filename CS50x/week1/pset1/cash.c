//Greedy Change Return

#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
//Take User Input, do while for positive number
    float dollar;
    do
    {
        dollar = get_float("Change owed: ");
    }
    while (dollar < 0);
        

//Convert dollar and cent to cents and round, remove imprecision
    int cent = round(dollar * 100);
    

    
//number of coins
    int coin = 0;

    if (cent > 24)
    {
        coin = floor(cent / 25);
        cent = cent % 25;
        
    }
    if (cent > 9)
    {
        coin = coin + (floor(cent / 10));
        cent = cent % 10;
    }
    if (cent > 4)
    {
        coin = coin + (floor(cent / 5));
        cent = cent % 5;
    }
    if (cent > 0)
    {
        coin = coin + (floor(cent / 1));
        cent = cent % 1;
    }
    
    printf("%i\n", coin);





//Total Coins
}
