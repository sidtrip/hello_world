def main():
    n = int(input("Enter a value:"))
    sum = 0
    while(n!=0):
        sum += n
        print("Running total is " + str(sum))
        print("")
        n = int(input("Enter a value:"))

if __name__ == '__main__':
    main()
