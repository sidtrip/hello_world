"""
Write your answer for Odd Numbers below here:
"""

def main():
    for i in range (100):
        odd = (i * 2) + 1
        # alt: for i in range(1 , 199, 2):
        print(odd)
        

if __name__ == "__main__:
    main()


"""
Write your answer for Can I Ride the Rollercoaster below here:
"""

def main():
    height = float(input("Enter height in meters: "))
    if height >= 1 and height <= 2:
        print("You can ride the roller coaster.")
    else:
        print("You can't ride the roller coaster")

if __name__ == "__main__:
    main()
