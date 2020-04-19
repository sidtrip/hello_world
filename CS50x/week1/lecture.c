#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int counter = get_int("put positive int\n");
    float x = 0;
    char y;
    bool z;

    counter = counter+1;
    counter +=1;
    counter ++;

/*This is a multi line comment, 
        wont autoclose unless I do so */
//This being a single line comment

    if(counter<10)
    {
        printf("counter is very small, single digit in fact\n counter= %i\n", counter);
    }
    
    else if(counter==10)
    {
        printf("counter=10\n");
    }
    
    else
    {
        printf("counter is greater than 10\n");
    }


    while(counter<100)
    {
        printf("%i\n", counter);
        counter ++;
    }

    for (int i=0; i<150 ; i++)
    {
        printf("good150");
        printf("true, 1, any number or anything other than 0, false: is always true");
    }    
}
