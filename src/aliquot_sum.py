"""
The sum of a number's proper divisors,
otherwise known as an aliquot sum.
"""

def aliquot_sum(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    print(sum)

# Should print 16
aliquot_sum(12)

# Should print 0
aliquot_sum(1)

