# https://www.hackerrank.com/challenges/ctci-recursive-staircase


step_sizes = [1, 2, 3]


def how_many(stair_length):
    if stair_length == 0:
        return 1
    if stair_length < 0:
        return 0
    return sum([how_many(stair_length - step_size) for step_size in step_sizes])

assert how_many(-11) == 0
assert how_many(1) == 1
assert how_many(3) == 4
assert how_many(7) == 44
print 'OK'
