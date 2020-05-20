# Data comes from Johns Hopkins Univeristy. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# You can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time
Each line in the file represents one day. The first value is confirmed cases on Jan 22nd.
The number of confirmed cases is "cumulative" meaning that it is the total number
of cases up until the current day. It will never go down! 
'''

ITALY_PATH = 'italy.txt'

# This directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'
REVERSAL_MAGIC_NO = 5

def main():
    italy = []
    count = 0
    prev_day_cases = 0
    new_cases_each_day = []
    reversal_counter = 0
    for line in open(ITALY_PATH):
        day_line_cases = int(line.strip())
        if day_line_cases:
            count += 1
        italy.append(day_line_cases)
        new_cases = day_line_cases - prev_day_cases
        new_cases_each_day.append(new_cases)
        if prev_day_cases < day_line_cases:
            reversal_counter += 1
            if reversal_counter > REVERSAL_MAGIC_NO:
                print("This country has reversed the trend, from a simplistic moder POV")
        prev_day_cases = day_line_cases
    print(italy)
    print(count)
    print(new_cases_each_day)
if __name__ == '__main__':
    main()
