import time
import random

from termcolor import colored

PHASE_TIME_S = 10

def main():
    print_intro()
    # Your solution goes here
    print(run_single_test(True))
    print(run_single_test(False))

def run_single_test(is_phase_1):
#fill with milestone 1
    #print colored word, match depending on param
    color_name = random_color_name()
    font_color = get_font_color(color_name, is_phase_1)
    print_in_color(color_name, font_color)
    #get user answer and return if got right
    response = input("What color ink is the word written in? ")
    return response == font_color
      

#get the color the text should be printed in - same as color_name
#if phase 1 or random if not
def get_font_color(color_name, should_match):
    #genfontcolor
    if should_match:
        return color_name
    
    #make sure color is not same as name
    font_color = random_color_name()
    
    while font_color == color_name:
        font_color = random_color_name()
    return font_color


def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')

def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink'])

def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()
