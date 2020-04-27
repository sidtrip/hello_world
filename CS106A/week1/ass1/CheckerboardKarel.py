from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    buggy for small worlds, work on it if need be
    """
    while left_is_clear():
        ckbd()
        if left_is_clear():
            turn_left()
            move()
            turn_right()


def ckbd():
    paint_corner(GRAY)
    move()
    row_checker()
    cmbk()
    if left_is_clear():
        turn_left()
        move()
        turn_right()
        row_checker()
        cmbk()

def row_checker():

    while front_is_clear():
        move()
        paint_corner(GRAY)
        if front_is_clear():
            move()

def cmbk():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
