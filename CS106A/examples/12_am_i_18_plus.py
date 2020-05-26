"""
a program that takes a person's age as input and determines if a person can vote or not, that is,
if he is older than 18 years old or not.
"""
AGE_THRESHOLD = 18

def main():
    age = input("Enter your age: ")
    age = float(age)
    if age <= AGE_THRESHOLD:
        print("Sorry, you can't vote yet!")
    else:
        print("You're old enough to vote!")
    print('')

if __name__ == '__main__':
    main()
