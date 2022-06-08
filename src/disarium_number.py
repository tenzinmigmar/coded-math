"""
A number is said to be the Disarium number when the sum
of its digit raised to the power of their respective
positions is equal to the number itself.
"""
import math

def is_disarium(number):
    digits = [int(i) for i in list(str(number))]

    sum = 0
    for index, item in enumerate(digits, start=1):
        sum += item ** index

    if sum == number:
        print("{} is a Disarium number!".format(number))
    else:
        print("{} is not a Disarium number!".format(number))

# Should output 25 is not a Disarium number!
is_disarium(25)

# Should output 175 is a Disarium number!
is_disarium(175)


