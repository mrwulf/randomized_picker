#!/usr/local/bin/python
import os
import random
from time import sleep
from art import text2art

names = [
    "Danna",
    "Mike",
    "Vince",
    "Anderson",
    "Matthew",
    "Sony",
    "Freeman",
    "Rakesh",
    "Eden",
]

def picker():
    iterations = 50
    previous_name = None

    for i in range(1, iterations):
        j = random.randint(0, len(names) - 1)

        name = names.pop(j)
        if i == iterations - 1:
            name += "!!!"

        print(text2art(name))

        sleep((i / iterations) ** 1.2)

        if previous_name:
            names.append(previous_name)

        previous_name = name

        if i != iterations - 1:
            os.system("clear")

if __name__ == "__main__":
    picker()
