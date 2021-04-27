#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = number * -1
    l = (new % 10) * -1
else:
    l = number % 10
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
elif l <= 5 and l != 0:
    print("Last digit of {} is {}".format(number, l) +
          " and is less than 6 and not 0")
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
