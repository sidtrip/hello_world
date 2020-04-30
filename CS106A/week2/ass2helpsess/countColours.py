"""
Ask user for as many colours as they can think of, in case they
enter'white', they are done.
Print out how many the user input
"""

def main():
    #get input from user
    colour = input("Enter a colour: ")
    colour_count = 1
    #keep getting until white
    while (colour != "white" ):
        colour = input("Enter a colour: ")
        colour_count += 1

    #track how many so far
    print("Total number of colours entered " + str(colour_count))







if __name__ == '__main__':
    main()