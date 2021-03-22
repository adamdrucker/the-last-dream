# //////////////////////////////////////
# *~* Abyssea Treasure Casket Game *~*
# ////////////////////////////////////

# Modules
# //////////////////////////
from random import randint
import time


# Random answer generated at start of sequence
result = str(randint(10, 99))


master_hint_list = []

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

    for char in i:

        print(char, end='')
        time.sleep(0.25)


# == First hint ==
def hint_sum():

    result_sum = int(result[0]) + int(result[1])

    print(f"You sense the sum of the two digits is {result_sum}.")

    # Append 1
    master_hint_list.append("1")


# == Second hint ==
def hint_int():

    digit_type_hint = randint(0, 1)
    first_dig = result[0]
    second_dig = result[1]

    if first_dig == second_dig:

        # Buffs from COR applied for this turn
        pr_str = "*~## PHANTOM ROLL! ##~*\n"
        phantom_print(pr_str)   # Calls stylized print func
        print("Buffs applied!")
        time.sleep(1)
        print("You sense the two digits are the same number.")

        # Append 2
        master_hint_list.append("2")
        time.sleep(1)

    elif digit_type_hint == 0 and int(first_dig) % 2 == 0:
        print("You sense the first digit is even.")

        # Append 3
        master_hint_list.append("3")
        time.sleep(1)

    elif digit_type_hint == 0 and int(first_dig) % 2 != 0:
        print("You sense the first digit is odd.")

        # Append 4
        master_hint_list.append("4")
        time.sleep(1)

    elif digit_type_hint == 1 and int(second_dig) % 2 == 0:
        print("You sense the second digit is even.")

        # Append 5
        master_hint_list.append("5")
        time.sleep(1)

    elif digit_type_hint == 1 and int(second_dig) != 0:
        print("You sense the second digit is odd.")

        # Append 6
        master_hint_list.append("6")
        time.sleep(1)


# == Third hint ==
def hint_range():

    g_than = int(result) - randint(10, 12)  # Produce random value 10-12 below the result
    l_than = int(result) + randint(10, 12)  # Produce random value 10-12 above the result

    # Block hint from being below MIN
    if g_than < 10:
        g_than = 10 + randint(randint(0, 2), randint(4, 6))
        return g_than

    # Block hint from being above MAX
    if l_than > 99:
        l_than = 99 - randint(randint(0, 2), randint(4, 6))
        return l_than

    # Move the below out of the func
    # --------------
    # if guess < result:
    #     print(f"You sense the answer is greater than {guess} and less than {l_than}.")
    # elif guess > result:    # Change to 'else'?
    #     print(f"You sense the answer is greater than {g_than} and less than {guess}.")


# ==== CALL FOR HINT ====
def hint_fetch():

    i = randint(0, 2)

    if i == 0:
        hint_sum()

    elif i == 1:
        hint_int()

    elif i == 2:  # Change to 'else'?
        hint_range()


# Init main program
# //////////////////////////////////////

def main():

    attempts = 0

    while attempts < 5:

        # Needs error handling for non-numeric input
        guess = input("Enter a number between 10 and 99: ")

        if hint_range() == "l_than":
            print(f"You sense the answer is greater than {guess} and less than {hint_range()}.")

            # Append 7
            master_hint_list.append("7")

        elif hint_range() == "g_than":
            print(f"You sense the answer is greater than {hint_range()} and less than {guess}.")

            # Append 8
            master_hint_list.append("8")

        # == Successful attempt ==
        if int(guess) == int(result):

            if int(guess) and int(result) == 43:

                # == Dialogue for 43 win==
                print("...")
                time.sleep(1.5)
                print(".......")
                time.sleep(2.5)
                print("Your attempt was successful. The sturdy pyxis emits a soft glow.")
                time.sleep(1)
                print("Although, a sudden cold chill runs down your spine...")
                time.sleep(2.5)
                print("...and you hear the faint sound of bells chiming in the distance.")
                time.sleep(3)
                print("Looking down at the chest, you hear a dull click as it pops open...")
                time.sleep(3)
                break

            else:

                # == Dialogue for regular win ==
                print("Your attempt was successful. The sturdy pyxis emits a soft glow.")
                time.sleep(2)
                print("A subtle warmth fills your palms.")
                time.sleep(1)
                print("You hear a click, and the chest pops open...")
                time.sleep(3)
                break

        # == Unsuccessful attempt ==
        elif int(guess) != int(result):

            attempts += 1

            if attempts in range(1, 4):
                print("The pyxis gently rattles in your hand.")
                time.sleep(1.5)
                hint_fetch()  # Call to retrieve random hint

            elif attempts == 4:
                print("The pyxis tremors with a strong vibration...")
                time.sleep(1.5)
                hint_fetch()  # Call to retrieve random hint

    if attempts == 5:

        # == Dialogue for 43 loss ==
        if result == 43:

            print("You have exceeded your allotted attempts. The correct answer was...")
            time.sleep(2.5)
            print(f"...the correct answer was {result}.")
            time.sleep(1.5)
            print("Your fingers start to grow cold, and your hands tremble.")
            time.sleep(1.5)
            print("Your vision blurs, as you feel something caught in your throat...")
            time.sleep(1.5)
            print("You seem to have forgotten what you were just doing, and return"
                  " to your travels...")
            time.sleep(3)

        else:

            # == Dialogue for regular loss ==
            print(f"You have exceeded your allotted attempts. The correct answer was {result}.")
            time.sleep(3)
            print("The sturdy pyxis slowly vanishes in front of your eyes...")
            time.sleep(1.5)
            print("You seem to have forgotten what you were just doing, and return"
                  " to your travels...")
            time.sleep(3)


main()