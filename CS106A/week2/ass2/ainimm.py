include random
#Incomplete, needs/requires more thinking

def main():
    stones = 20


    while stones > 0:
        print("There are " + str(stones) + "stones left")

        n = int(input("Player would you like to remove 1 or 2 stones?"))
        while (n != 1 or 2):
            n = int(input("I said 1 or 2"))
        stones -= n

        print("There are " + str(stones) + "stones left")
        if (stones % 3 == 1):
            n= random.randint(1,2)
        elif (stones % 3 == 2):
            n= 1
        else:
            n = 2

        print("Computer picks " + str(n) + " stones")
