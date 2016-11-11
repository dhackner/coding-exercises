# https://www.hackerrank.com/challenges/ctci-recursive-staircase


step_sizes = [1, 2, 3]
answers = {0: 1}


def how_many(stair_length):
    if stair_length < 0:
        return 0
    elif stair_length not in answers:
        answers[stair_length] = sum([how_many(stair_length - step_size) for step_size in step_sizes])

    return answers[stair_length]

assert how_many(-11) == 0
assert how_many(1) == 1
assert how_many(3) == 4
assert how_many(7) == 44
print 'OK'
