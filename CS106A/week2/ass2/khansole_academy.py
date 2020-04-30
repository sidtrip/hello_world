"""
File: khansole_academy.py
-------------------------
—a program that helps other people learn!
In this problem, you’ll write a program in the file khansole_academy.py that randomly
generates simple addition problems for the user, reads in the answer from the user, and then
checks to see if they got it right or wrong, until the user appears to have mastered the
material
"""

MASTERY_NO = 3
#no of questions to be correct to stop asking qs
import random


def main():

    # 1> Generate random(2 digit) addition problems.

    inarow = 0
    while(inarow < MASTERY_NO):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)

        # 2> Read user input for answers.
        print("What is " + str(num1) + " + " + str(num2) + "?")
        ans = int(input("Your answer: " ))
        # 3> Check for correctness of answer input.

        if (ans == num1 + num2):
            inarow += 1
            print("Correct! You've gotten " + str(inarow)+" correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(num1+num2))
            inarow = 0
    print("Congratulations! You mastered addition.")

        # 4> Repeat until master_no


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
