# Functions for Pyxis guess
# /////////////////////////

import time


def phantom_print(i):
    # called if both digits are the same
    for char in i:
        print(char, end='')
        time.sleep(0.25)


# Hints
# /////

def hint_sum(i):
    # returns sum of two-digit answer
    print(f"You sense the sum of the two digits is {i}.")

# def hint_int_same_digit()
# def hint_int_type_zero_first_even()
