#Hospital


from karel.stanfordkarel import *

def main():
   """
   pre:on supplies beeper, facing east.
   post: one block east to supplies beeper, facing east.
   """
   while front_is_clear():
      if beepers_present():
         pick_beeper()
         build_hospital()
      if front_is_clear():
         move() 
         #needs to be facing east
   turn_around()
   while front_is_clear():
      move()
   turn_around()
   
def build_hospital():
      """
      precondition:picked a beeper facing east
      postcondition: facing east
      """
      turn_left()
      put_3()
      turn_right()
      move()
      turn_right()
      put_3()
      turn_left()

def put_3():
   """
   pre: karel is facing direction of beeper at position 1
   post: at beeper 3 facing away from beeper1 or base
   """
   for i in range(2):
      put_beeper()
      move()
   put_beeper()
   
def turn_right():
   for i in range(3):
      turn_left()
   
def turn_around():
   for i in range(2):
      turn_left()
