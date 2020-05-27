def main():
    year = int(input("Please, input a year: "))
    if not(year % 4):
        if not(year % 100):
            if not(year % 400):
                print("A given year {} is a leap year".format(year))
            else:
                print("A given year {} is a NOT leap year".format(year))
        else:
            print("A given year {} is a leap year".format(year))
    else:
        print("A given year {} is NOT a leap year".format(year))
    print("----------------------x-------------------")

if __name__ == '__main__':
    main()