from random import randint

guessesTaken = 0
result = randint(1, 9)

print("While travelling across a field you stumble upon a small, sturdy pyxis amidst a patch of tall grass.")
print("It appears to be locked tight by some force beyond your reckoning.")
print("A soft whisper echoes in your mind.")
print('"You have three attempts to open the chest by guessing the combination..."')

while guessesTaken < 3:
    guess = input("Enter a number: ")
    if int(guess) == int(result):
        print("You guessed correctly. The sturdy pyxis emits a soft glow. You hear a click, and the chest pops open...")
        break
    elif guess != result:
        guessesTaken += 1
        if int(guess) < int(result):
            print(f"You sense the answer is higher than {guess}.")
            continue
        elif int(guess) > int(result):
            print(f"You sense the answer is lower than {guess}.")
            continue

if guessesTaken == 3:
    print(f"You exceeded your allotted guesses. The correct answer was {result}.")
    print("The sturdy pyxis slowly vanishes in front of your eyes...")
