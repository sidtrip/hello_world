from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Finding the midpoint of the bottom row using the property of a triangle that:
    an angle bisector of a triangle also bisects the face opposite to the angle

    """

    while front_is_clear():
        move()
        turn_left()
        move()
        turn_right()
    turn_right()
    #Reaching the apex of right angled isosceles triangle.

    while front_is_clear():
     #loop for reaching to base of opposite side
        for i in range(2):
            #loop to bisect, 2 moves on y coordinate, while 1 on the other
            if front_is_clear():
                move()
            else:
                #but we want to put beeper if front is blocked, when we reach base
                put_beeper()

        turn_right()
        move()
        #single move on x coordinate
        turn_left()
    put_beeper()
    #if front ends up being clear, we want to be putting beeper.

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()



    """
    
    #ALTERNATE METHOD
    #INTERESECTING DIAGONALS
    
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        turn_left()
        move()
        turn_right()
        put_beeper()

    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while no_beepers_present():

        move()
        turn_left()
        if no_beepers_present():
            move()
            turn_right()

    if not_facing_south():
        turn_right()

    while front_is_clear():
        move()
    put_beeper()


    #garbage collection
    turn_right()
    while front_is_clear():
        move()
    turn_around()
    pick_beeper()

    while front_is_clear():
        move()
        pick_beeper()
        turn_left()
        move()
        turn_right()
        pick_beeper()


def turn_around():
    for i in range (2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

    """

    """
    #ALTERNATE3
    #PINGPONG METHOD
    #infinite loop at end

    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

    turn_around()
    if front_is_clear():
        pick_beeper()
        while front_is_clear():
            move()
        pick_beeper()
        turn_around()
        while front_is_clear():
            move()
            if no_beepers_present():
                turn_around()
                move()
                if front_is_clear():
                    move()
                    if beepers_present():
                        turn_around()
                        move()
                        turn_around()
                        if beepers_present():
                            pick_beeper()

    
def turn_around():
    for i in range(2):
        turn_left()

    """

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
