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

## TESTS
def assert_equal(result, expected):
    from sys import _getframe

    msg = 'FAIL: Line {} got: {} expecting: {}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))

if __name__ == "__main__":
    # Case 4
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    # Case 1
    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    # Case 2
    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    # Case 3
    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')