"""
FizzBuzz Rules

1. If position is divisible by 3: say Fizz
2. If position is divisible by 5: say Buzz
3. If position is divisible by 3 and 5: say FizzBuzz
4. Otherwise say the position
"""
from functools import partial

divisible_by = lambda base, num: num % base == 0
divisible_by_3 = partial(divisible_by, 3)
divisible_by_5 = partial(divisible_by, 5)

def robot(pos):
    say = str(pos)

    if divisible_by_3(pos) and divisible_by_5(pos):
        say = 'fizzbuzz'
    elif divisible_by_5(pos):
        say = 'buzz'
    elif divisible_by_3(pos):
        say =  'fizz'

    return say
