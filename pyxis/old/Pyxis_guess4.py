# //////////////////////////////////////////
# *~* Abyssea Treasure Casket Game *~*
# c h o i c e  g u i d e s  f a t e #
# ///////////////////////////////////////

# Modules
# //////////////////////////////////////
from random import randint
import time

# Init main variables
# //////////////////////////////////////
attempts = 0                                # Counter for attempts
result = str(randint(10, 99))               # Random answer generated at start of sequence


# Init main program
# //////////////////////////////////////

# def main():

# Opening dialogue
# //////////////////////////////////////
print("While travelling across a field you stumble upon a small, sturdy pyxis amidst a patch of tall grass.")
time.sleep(5)
print("It appears to be locked tight by some force beyond your reckoning.")
time.sleep(4)
print("A soft whisper echoes in your mind.")
time.sleep(2)
print('"You have five attempts to open the chest by guessing the combination..."')
time.sleep(4)


'''         There are 5 attempts to surmise the combination 
            to a locked chest, with each subsequent 
            incorrect guess prompting
            a hint to be displayed.
'''

# -------------------------------------------------------------------------------------

iAction = input("1) Enter a combination\n"
                "2) Examine the lock\n"
                "Enter 1 to attempt a combination, or 2 to examine the locking mechanism: ")

# -------------------------------------------------------------------------------------


def hint_fetch():
    return randint(0, 2)


# Initial hint given -- Turn this into a function called via choose_action ------------
def init_hint():
    while attempts == 0:
        print("You examine the locking mechanism with a discerning eye.")
        time.sleep(1.5)
        hint_fetch()  # Calls hint_fetch function to procure a random hint
        break


# First hint

def hint_sum():
    result_sum = int(result[0]) + int(result[1])
    print(f"You sense the sum of the two digits is {result_sum}.")


# Second hint

def hint_int():
    digit_type_hint = randint(0, 1)
    first_dig = result[0]
    second_dig = result[1]
    if digit_type_hint == 0 and int(first_dig) % 2 == 0:
        print("You sense the first digit is even.")
        time.sleep(1)
    elif digit_type_hint == 0 and int(first_dig) % 2 != 0:
        print("You sense the first digit is odd.")
        time.sleep(1)
    elif digit_type_hint == 1 and int(second_dig) % 2 == 0:
        print("You sense the second digit is even.")
        time.sleep(1)
    elif digit_type_hint == 1 and int(second_dig) != 0:
        print("You sense the second digit is odd.")


# Third hint
# Need to prevent hints from displaying values <10 and >99
# "guess" here is out of scope with the defined variable (below this section)


def hint_range():
    g_than = int(result) - randint(10, 12)  # Produces a value randomly between 10-12 below the result
    l_than = int(result) + randint(10, 12)  # Produces a value randomly between 10-12 above the result
    if guess < result:
        print(f"You sense the answer is greater than {guess} and less than {l_than}.")
    elif guess > result:
        print(f"You sense the answer is less than {guess} and greater than {g_than}.")


# Turn this into a function and call it via choose_action -----------------------------------
def enter_combo():
    while attempts < 5:
        guess = input("Enter a number between 10 and 99: ")
        # ==Successful attempt==
        if int(guess) == int(result):
            print("Your attempt was successful. The sturdy pyxis emits a soft glow.")
            time.sleep(1)
            print("You hear a click, and the chest pops open...")
            break

        # Unsuccessful attempt
        if guess != result:
            attempts += 1
            print("The pyxis gently rattles in your hand.")
            time.sleep(1.5)
            hint_fetch()  # Main call to retrieve random hints
# -----------------------------------------------------------------------------------------


if hint_fetch == 0:
    hint_sum()
elif hint_fetch == 1:
    hint_int()
elif hint_fetch == 2:
    hint_range()


def choose_action(x):
    if int(x) == 1:
        enter_combo()
    elif int(x) == 2:
        init_hint()
    else:
        print("Enter 1 to attempt a combination, or 2 to examine the locking mechanism.")


choose_action(iAction)      # Pass input through function


# Chest disappears if the answer is not found within five guesses
if attempts == 5:
    print(f"You have exceeded your allotted attempts. The correct answer was {result}.")
    print("The sturdy pyxis slowly vanishes in front of your eyes...")
