

def main():
    n = int(input("Enter a number for hailstone sequence: "))
    counter = 0
    while (n != 1):
        if (not(n % 2)):
        #even clause
            print(str(n) + " is even, so I take half: ", end = "")
            n /= 2
            n = int(n)
            print(n)
        else:
            print(str(n) + " is odd, so I make 3n+1: ", end= "")
            n = (n * 3 + 1)
            print(n)
        counter += 1
    print("This process took " + str(counter) + " steps to reach 1" )







if __name__ == '__main__':
    main()


