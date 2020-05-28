"""
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in

format.

Constraints

Output Format

Output the correct day in capital letters. 

_____CODES_____
"""

import calendar
import sys

stdin = sys.stdin


# TODO 1: "Calendar Module"
def print_week_day(month, day, year):
    week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    weekday = calendar.weekday(year, month, day)
    print(week[weekday].upper())
    return 0


def main():
    month, day, year = stdin.readline().lstrip().rstrip().split()
    # inp_str = input().lstrip().rstrip()
    print_week_day(int(month), int(day), int(year))

if __name__ == '__main__':
    main()
