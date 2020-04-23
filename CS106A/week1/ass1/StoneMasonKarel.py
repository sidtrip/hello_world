from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""




def main():
    """
    This stone mason karel builds the pillars by combing the pillars
    bottom up. Choosing this way of solving because of the ideology
    taught in lecture that for initial programming days we must use
    simplicity over effeciency.
    """

    build_pillar()
    while front_is_clear():
        for i in range(4):
            move()
        build_pillar()

def build_pillar():
    """
    pre: facing east while standing at the bottom of a pillar.
    post: facing east while on bottom and the pillar is repaired.
    """
    turn_left()
    beeper_think()
    while front_is_clear():
        move()
        beeper_think()
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def beeper_think():
    #decision making of beeper, placing only if no beepers are present

    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

"""

#Try other way

    while front_is_clear()
        left_hand_pillar()
        move_next()
        while 
        turn_right()
        build_pillar()
        move_next()

def build_pillar():
    
"""







# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
