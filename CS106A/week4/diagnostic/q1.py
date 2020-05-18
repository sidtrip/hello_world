"""
42

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2

def main():
    n = 42
    divide_and_round(n)
    print(n)  # should print 21
"""

"""
Part B: 
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    n = int(n)
    # division always returns a float, so truncating to get a float,
    # we can alternately achieve same functionality with int division op // 
    return n
    # we need the function to turn back the value calculated to the calee.

def main():
    n = 42
    divide_and_round(n)
    print(n) 
