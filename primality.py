# https://www.hackerrank.com/challenges/ctci-big-o


import math


def is_prime(n):
    if n <= 1:
        return False
    for test_number in range(2, int(math.sqrt(n)) + 1):
        if n % test_number == 0:
            return False

    return True


assert not is_prime(12)
assert is_prime(5)
assert is_prime(7)
assert not is_prime(9)  # Test an exact square root being the only divisor
print 'OK'
