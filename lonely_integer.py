# https://www.hackerrank.com/challenges/ctci-lonely-integer


def lonely_integer(a):
    found = set()
    for number in a:
        if number in found:
            found.remove(number)
        else:
            found.add(number)
    return found.pop()

assert lonely_integer([1]) == 1
assert lonely_integer([1, 1, 2]) == 2
assert lonely_integer([0, 0, 1, 2, 1]) == 2
print 'OK'
