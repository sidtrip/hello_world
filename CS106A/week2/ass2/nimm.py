"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate
taking stones until there are zero left. The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
"""


def main():
    stone = 20
    turn = 1
    #initializing and declaring stones and player number
    while(stone > 0):
        print("There are " + str(stone) + " stones left")

        n = int(input("Player " + str(turn) + " would you like to remove 1 or 2 stones? "))
        #n is number of stones to be removed 1 or 2
        while(n < 1 or n > 2):
            n = int(input("Please enter 1 or 2: "))
        print("")
        stone -= n
        #decreasing picked stones from total
        if (turn == 1):
            turn = 2
        else:
            turn = 1
    #since the player who pics last loses winners are swapped in loop too
    print("Player " + str(turn) + " wins!")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
