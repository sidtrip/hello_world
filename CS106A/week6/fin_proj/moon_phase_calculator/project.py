# Importing functions to get present date.
from datetime import date
import tkinter

"""
    This program asks user for a date input and bypasses the input if they want with current date from the
    computer to show a Graphical Moon Phase Image using tkinter with data field overlay on the canvas of
    Moon Age(in days), Lumination(in percentage), Name of the Moon Phase(8/9 Phase Naming System)
    The comments are in the form:
    #Comment 
        <for code>
    #Comment
        <for code>
    PS: There are a few innate assumptions here:-
        - Showing moon-phase for Northern Hemisphere
        - Not compensating for TimeZones, so there might be a slight
            difference in your date and GMT.
        - Taking moons orbit as circular, Leads to a minor error as we
            go far from base JulianDate taken for comparision(6JAN2000)
        - Can't go before the Julian date to compare
        
"""

JD_FOR_01062000 = 2451549.5     # Julian Day ref for full moon calculation/comparision6JAN2000 12:24:01 NEW
OLD = 29.53                     # Lunar Phase Cycle- No of days New Moon to New Moon
NEW = 0                         # New moon Day
WAX_CRE = OLD/8                 # Other Moon Phase Names Consts and days they fall on.....
FIRST_QUART = OLD/4
WAX_GIBB = (3 * OLD) / 8
FULL = OLD/2
WAN_GIBB = (5 * OLD) / 8
LAST_QUART = (3 * OLD) / 4
WAN_CRE = (7 * OLD)/8

WIDTH = 380                     # Width and Height of canvas Used respectively
HEIGHT = 380


def main():
    print("Enter Date Month and Year in format DD/MM/YYYY; eg. for 1st Feb 2030: '1/2/2030' ")
    today = input(" PRESS ENTER FOR TODAY: ")
    if today == '':
        today = date.today()    # Fetches Computer date if user bypasses by pressing Enter/Return
        today = today.strftime("%d/%m/%Y")
    today = today.split('/')    # making a list out of three diff values, splitting on fwd slashes

    y = int(today[2])           # saving year/month/date from array to variables
    m = int(today[1])
    d = int(today[0])

    canvas = make_canvas(WIDTH, HEIGHT, 'MoonPhase')
    # Making rectangle on canvas with few pixel margins
    canvas.create_rectangle(1, 10, WIDTH - 2, HEIGHT - 2, fill="black", outline="black")
    # Putting Date Chosen on top of the Canvas
    canvas.create_text(WIDTH - 70, 4, anchor='w', font='Arial 12', text=str(d) + ' / ' + str(m) + ' / ' + str(y))
    # Creating a basic circle for Moon
    canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='white')

    moon_age = calculate_moon_age(d, m, y)
    name = moon_name(moon_age, canvas)
    lumination = lum_pc(moon_age)

    print(name)
    print("LUMINATION ~ " + str(lumination) + " %")
    print("MOON AGE: " + str(truncate_decimal1(moon_age)))

    canvas.create_text(3, HEIGHT - 10, anchor='w', font='Courier 16', text=name, fill="white")
    canvas.create_text((WIDTH / 2) - 50, 28, anchor='w', font='Arial 11', text='LUMINATION: ' + str(lumination) + " %", fill="white")
    canvas.create_text((WIDTH / 2) - 50, 16, anchor='w', font='Arial 11', text='MOON AGE: ' + str(truncate_decimal1(moon_age)) + " day/s" , fill="white")

    canvas.mainloop()


def calculate_moon_age(d, m, y):
    # Using technique from: https://www.subsystems.us/uploads/9/8/9/4/98948044/moonphase.pdf
    if m == 1 or m == 2:        # If month is Jan or Fec Subtract 1 from year and add 12 to month
        y = y-1
        m = m+12
    # Calculates Julian Date for date input for comparision from the known New Moon
    a = y // 100
    b = a // 4
    c = 2 - a + b
    e = int(365.25 * (y + 4716))
    f = int(30.6001 * (m + 1))
    # Julian date for Input
    jd = c + d + e + f - 1524.5
    # No of days since 6JAN2000(JD constant, known New Moon)
    day_since_new_moon = jd - JD_FOR_01062000
    # Number of new moons since 6JAN2000
    new_moons = day_since_new_moon / OLD
    # Day factor
    day_factor = new_moons % 1  # Dropping whole Number
    # Number of days into cycle
    days_into_cycle = day_factor * OLD
    return days_into_cycle


def moon_name(days_into_cycle, canvas):
    # This function compares the no of days the input date is from new moon with midpoint
    # of the average of standard moonphase days to get us to know what the phase is.
    if days_into_cycle < mid(NEW, WAX_CRE):
        name = "NEW MOON"
        # Printing a gray oval to cover whole moon drawn in main as grey
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='grey')
    elif days_into_cycle < mid(WAX_CRE, FIRST_QUART):
        name = "WAXING CRESCENT"
        # Printing a black oval to cover partial moon drawn in main to show phase.
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 3), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
    elif days_into_cycle < mid(FIRST_QUART, WAX_GIBB):
        name = "FIRST QUARTER"
        canvas.create_rectangle(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 2), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
    elif days_into_cycle < mid(WAX_GIBB, FULL):
        name = "WAXING GIBBOUS"
        # Overwriting moon drawn in main as black
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
        # Drawing a new oval moon with 75% illumination
        canvas.create_oval(WIDTH / 4, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='white')
    elif days_into_cycle < mid(FULL, WAN_GIBB):
        name = "FULL MOON"
    elif days_into_cycle < mid(WAN_GIBB, LAST_QUART):
        name = "WANING GIBBOUS"
        # Overwriting moon drawn in main as black
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
        # Drawing a new oval moon with 75% illumination
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 4), HEIGHT - (HEIGHT / 8), outline='black', fill='white')
    elif days_into_cycle < mid(LAST_QUART, WAN_CRE):
        name = "LAST QUARTER"
        canvas.create_rectangle(WIDTH / 2, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
    elif days_into_cycle < mid(WAN_CRE, OLD):
        name = "WANING CRESCENT"
        canvas.create_oval(WIDTH / 3, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='black')
    else:
        name = "NEW/OLD MOON"
        canvas.create_oval(WIDTH / 8, HEIGHT / 6, WIDTH - (WIDTH / 8), HEIGHT - (HEIGHT / 8), outline='black', fill='grey')
    return name


def lum_pc(days_into_cycle):
    # Day 0 is New Moon with lumination 0% day Day 14 will be Full Moon 100% lumnation and Day 29 will be New/old again.
    lumn_pc = percent(days_into_cycle)
    # Truncating_decimals
    lumn_pc = truncate_decimal1(lumn_pc)
    return lumn_pc


def mid(arg1, arg2):
    # This function Calculates Average of two numbers, midpoint of two days in this case.
    return (arg1 + arg2) / 2


def percent(arg1):
    if arg1 <= FULL:
        return (arg1 / FULL) * 100
    else:
        return ((OLD - arg1)/FULL) * 100


def truncate_decimal1(arg1):
    # Truncate decimals to one digit after decimal point using simple multiplication factor, division and truncating
    arg1 = int(arg1 * 10)
    arg1 = arg1 / 10
    return arg1



# MILESTONES
"""
Flow of the Project:
Find and implement a way to Calculate Moonage/Phase.
Read Date and time from computer and compute Moon Age
Print Days and Lumination Percentage to Console
Name Moon as New, Full, First or Last Quarter
Take Date as User Input, read today's date if no input provided.
Create a canvas and Print Console Text on it.
Draw Moon using a tkinter Function
Represent correct moon-phase at canvas using tkinter.
Try making a clickable button for previous/next days.(COUDN'T DO IT)
Reformat code and see if things are cohesive.
"""


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
    return canvas

if __name__ == '__main__':
    main()