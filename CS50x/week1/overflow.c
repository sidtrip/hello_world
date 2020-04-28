#include <unistd.h>
#include <stdio.h>

int main (void)
{
    
    for (int i=1; ; i*=2)
    {
        printf("%i\n", i);
        sleep(1);
    }
}
