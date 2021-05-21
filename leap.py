# File: isabelle_bretl_hw1.py
# Author: Isabelle Bretl
# Date: 04.11.2021
# Input: The user will enter a year
# Output: The program will print a statement regarding whether
# or not the given year is a leap year


def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False