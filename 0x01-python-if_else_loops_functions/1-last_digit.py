#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = number * -1
    new = (new % 10) * -1
else:
    number = number
if new > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, new))
elif new < 5 and last != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, new))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, new))
