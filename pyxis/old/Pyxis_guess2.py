# Abyssea Treasure Casket Game
# c h o i c e  g u i d e s  f a t e

from random import randint
import time

# Counter for attempts and random answer generated at start of sequence
attempts = 0
result = str(randint(10, 99))

print("While travelling across a field you stumble upon a small, sturdy pyxis amidst a patch of tall grass.")
# time.sleep(5)
print("It appears to be locked tight by some force beyond your reckoning.")
# time.sleep(4)
print("A soft whisper echoes in your mind.")
# time.sleep(2)
print('"You have five attempts to open the chest by guessing the combination..."')
# time.sleep(4)

'''There are 5 attempts to surmise the combination to a locked chest, with each subsequent incorrect guess prompting
    a hint to be displayed.'''

# Initial hint given -- rather than using the below, have a random type of hint generated each time
while attempts == 0:
    print("You examine the locking mechanism with a discerning eye.")
    time.sleep(1.5)
    first_dig = result[0]
    if int(first_dig) % 2 == 0:
        print("You sense the first digit is even.")
        time.sleep(1)
    else:
        print("You sense the first digit is odd.")
        time.sleep(1)
    break

while attempts < 5:
    guess = input("Enter a number between 10 and 99: ")
    # ==Successful attempt==
    if int(guess) == int(result):
        print("Your attempt was successful. The sturdy pyxis emits a soft glow.")
        time.sleep(1)
        print("You hear a click, and the chest pops open...")
        break

    # ==Unsuccessful attempt==
    if guess != result:
        attempts += 1
        print("The pyxis gently rattles in your hand.")
        time.sleep(1.5)
        # Make hint_fetch call here to retrieve random hints
        def hint_fetch(num):
            if num == 0:
                g_than = int(result)-randint(10, 12)  # Produces a value randomly between 10-12 below the result
                l_than = int(result)+randint(10, 12)  # Produces a value randomly between 10-12 above the result
                print(f"You sense the answer is greater than {g_than} and less than {l_than}.")
            if num == 1:
                result_sum = int(result[0]) + int(result[1])
                print(f"You sense the sum of the two digits is {result_sum}.")
            if num == 2:
                second_dig = result[1]
                if int(second_dig) % 2 == 0:
                    print("You sense the second digit is even.")
                else:
                    print("You sense the second digit is odd.")

        hint_fetch(randint(0, 2))  # Calls function to produce a hint


# The chest disappears if the answer is not found within five guesses
if attempts == 5:
    print(f"You have exceeded your allotted attempts. The correct answer was {result}.")
    print("The sturdy pyxis slowly vanishes in front of your eyes...")
