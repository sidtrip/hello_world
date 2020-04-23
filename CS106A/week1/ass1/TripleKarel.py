from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    For simplicity in decomposition naming a singular
    function 'paint all buildings' here so that
    decomposition looks intuitive. Rather than a for
    loop jumping out of nowhere.
    """
    paint_all()

def paint_all():
    """
    pre: at init position facing direction of movement
    post: one corner ahead of last beeper painted
    """
    for i in range(3):
        paint_b()
        #paint building function
        turn_right()

def paint_b():
    """
    precondition: karel on initial position on a box facing direction of movement
                on side adjacent to the 'wall not to be painted' while wall on left.
    postcondition: karel moving one step ahead of previous box and facing initial
                position for next box
    """
    for i in range(2):
        paint_wall()
        turn_left()
        move()
    paint_wall()


def paint_wall():
    """
        pre: karel is at starting position on a wall with wall on left.
        post: karel is one block ahead of edge after painting a complete wall.
    """
    while left_is_blocked():
        put_beeper()
        move()


def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
