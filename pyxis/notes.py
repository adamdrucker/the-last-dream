import random
from random import randint

answer = randint(1, 10)

mylist = [0,1,2,3,4,5,6]

mydict = {
    0: "hint_sum",
    1: "hint_int1",
    2: "hint_int2",
    3: "hint_int3",
    4: "hint_int4",
    5: "hint_range1",
    6: "hint_range2"
}

guess = input("Enter a number: ")

if guess == answer:
    print("Correct!")
    exit()

while guess != answer:

    if len(mylist) == 0:
        break

    rem = random.choice(mylist)
    print(mydict[rem])
    mylist.remove(rem)
    print(f"mylist = {mylist}")
    print("Incorrect, try again: ")
    guess = input("Enter a number: ")

# The point of this is to have a list of values to correspond to each individual hint able to be given. Once that hint is given, it's corresponding number is removed from the
# list so it cannot be given a second time in the same game. A hint will be drawn at random, the func called, it's value removed from the list, and so on.

