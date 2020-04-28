#include <cs50.h>
#include <stdio.h>

int main (void)
{

  int n = get_int("N: \n");

  if (n%2==0)
  {
      printf("N is EVEN");
  }

  else
  {
      printf("N is ODD\n");
  }

}
