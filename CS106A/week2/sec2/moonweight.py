"""
Write a program to prompt the user for a weight on earth
and print the equivalent weight on the moon.
"""

MOON_MULTIPLE = 0.165
#weight on moon is 16.5% of that from earth

def main():
    # 1) Get input weight from user.
    earth_weight = input("Enter a weight on earth: ")
    
    # We need earth weight to be a number
    earth_weight = float(earth_weight)
    # 2) Calculate weight on moon.
    moon_weight = earth_weight* MOON_MULTIPLE
    
    # 3) Print the moonweight to the user.
    print("The Weight on Moon: " + str(moon_weight))
    

if __name__ == '__main__':
    main()
