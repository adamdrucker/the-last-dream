# //////////////////////////////////////
# *~* Abyssea Treasure Casket Game *~*
# ////////////////////////////////////

from random import randint
import random
import time


# Random answer generated at start of sequence
result = str(randint(10, 99))


master_hint_list = [1, 2, 3, 4, 5, 6, 7, 8]

'''     1 = hint_sum 1
        2 = hint_int 1
        3 = hint_int 2
        4 = hint_int 3
        5 = hint_int 4
        6 = hint_int 5
        7 = hint_range 1
        8 = hint_range 2
'''


def phantom_print(i):

    # Stylizes text passed in
    # Used for Phantom Roll

    for char in i:
        print(char, end='')
        time.sleep(0.25)


# ==== CALL FOR HINT ====
def hint_fetch():                           # This may need to be passed into hint_call
    # Pulls random item from master list
    i = random.choice(master_hint_list)
    return i


def hint_sum():
    result_sum = int(result[0]) + int(result[1])
    print(f"You sense the sum of the two digits is {result_sum}.")

def hint_int():
    # Some code

def hint_call(i):

    """ This is going to be one massive function calling all hints
        based on the digit passed in
        Numbers will then be removed from the master list
    """

    # Variables for hint_int hints

    digit_type_hint = randint(0, 1)
    first_dig = result[0]
    second_dig = result[1]

    if i == 1:

        # Hint 1

        hint_sum()
        master_hint_list.remove(1)

    elif i == 2:

        # Hint 2

        hint_int()








def main():

    inp = input("Press ENTER or 'q' to quit: ")

    while inp != "q":
        number = hint_fetch()
        print(f"Your random number is: {number}")

        print(master_hint_list)

        inp = input("Press ENTER or 'q' to quit: ")


if __name__ == '__main__':
    main()