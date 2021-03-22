from random import randint
import random
import time


result = str(randint(10, 99))


# // Main //

def main():

    # // Hint variables //

    fetch_list = ["hint_sum", "hint_int", "hint_range"]
    result_sum = int(result[0]) + int(result[1])
    digit_type_hint = randint(0, 1)
    first_dig = result[0]
    second_dig = result[1]



    # // Stylized print function //

    def phantom_print(i):
        for char in i:
            print(char, end='')
            time.sleep(0.25)


    # // Hints //

    def hint_sum():

        # This function should only be called ONCE per game

        print(f"You sense the sum of the two digits is {result_sum}.")


    def hint_range():

        # This function can be called MULTIPLE times per game, non-consecutively

        g_than = int(result) - randint(10, 12)  # Produce random value 10-12 below the result
        l_than = int(result) + randint(10, 12)  # Produce random value 10-12 above the result

        # Block hint from being below MIN
        if g_than < 10:
            g_than = 10 + randint(randint(0, 2), randint(4, 6))

        # Block hint from being above MAX
        if l_than > 99:
            l_than = 99 - randint(randint(0, 2), randint(4, 6))

        if guess < result:
            print(f"You sense the answer is greater than {guess} and less than {l_than}.")
        elif guess > result:
            print(f"You sense the answer is greater than {g_than} and less than {guess}.")


    def hint_int():

        # This function can be called MULTIPLE times per game, non-consecutively
        # Each individual hint should only be called ONCE

        hint_list = [1, 2, 3, 4, 5]
        i = random.choice(hint_list)


        if i == 1 and first_dig == second_dig:

            # // Buffs from COR applied for this turn //
            pr_str = "*~## PHANTOM ROLL! ##~*\n"
            phantom_print(pr_str)
            print("Buffs applied!")
            time.sleep(1)
            print("You sense the two digits are the same number.")
            hint_list.remove(1)
            time.sleep(1)



        elif i in [1, 2, 3, 4, 5]:
            if digit_type_hint == 0 and int(first_dig) % 2 == 0:
                print("You sense the first digit is even.")
                hint_list.remove(i)
                time.sleep(1)

            elif digit_type_hint == 0 and int(first_dig) % 2 != 0:
                print("You sense the first digit is odd.")
                hint_list.remove(i)
                time.sleep(1)

            elif digit_type_hint == 1 and int(second_dig) % 2 == 0:
                print("You sense the second digit is even.")
                hint_list.remove(i)
                time.sleep(1)

            elif digit_type_hint == 1 and int(second_dig) != 0:
                print("You sense the second digit is odd.")
                hint_list.remove(i)
                time.sleep(1)



    # // Call for hint //

    def hint_fetch():

        i = random.choice(fetch_list)

        if i == "hint_sum":
            hint_sum()
            # Only call hint_sum once per game
            fetch_list.remove("hint_sum")

        elif i == "hint_int":
            hint_int()

        elif i == "hint_range":
            hint_range()

        print(fetch_list)




    # // Attempts //

    attempts = 0

    while attempts < 5:

        # // Input scrubbing //
        value = 0
        while value == 0:
            try:
                guess = input("Enter a number between 10 and 99: ")

                if guess.isdigit() != True:
                    print("Please enter only numerical values.")
                    value = 0
                else:
                    value = 1

            except ValueError:
                print("Please enter only numerical values.")
                #value = 0

        # // Successful attempt //
        if int(guess) == int(result):

            if int(guess) and int(result) == 43:

                # // Dialogue for 43 win //
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

                # // Dialogue for regular win //
                print("Your attempt was successful. The sturdy pyxis emits a soft glow.")
                time.sleep(2)
                print("A subtle warmth fills your palms.")
                time.sleep(1)
                print("You hear a click, and the chest pops open...")
                time.sleep(3)
                break

        # // Unsuccessful attempt //
        elif int(guess) != int(result):

            attempts += 1

            if attempts in range(1, 4):
                print("The pyxis gently rattles in your hand.")
                time.sleep(1.5)
                hint_fetch()  # Call to retrieve random hint --> pass 'result' in?

            elif attempts == 4:
                print("The pyxis tremors with a strong vibration...")
                time.sleep(1.5)
                hint_fetch()  # Call to retrieve random hint

    if attempts == 5:

        # // Dialogue for 43 loss //
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

            # // Dialogue for regular loss //
            print(f"You have exceeded your allotted attempts. The correct answer was {result}.")
            time.sleep(3)
            print("The sturdy pyxis slowly vanishes in front of your eyes...")
            time.sleep(1.5)
            print("You seem to have forgotten what you were just doing, and return"
                  " to your travels...")
            time.sleep(3)


if __name__ == '__main__':
    main()
