"""
File: sentinelloop.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

def main():
    total = 0
    num = int(input("Enter a number: "))

    while (num !=  -1):
        total += num
        num = int(input("Enter the other number: "))

    print("total is " + str(total))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()