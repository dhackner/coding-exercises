# https://www.hackerrank.com/challenges/angry-professor


def cancel_or_nah(threshold, times):
    return 'YES' if len(filter(lambda x: x <= 0, times)) < threshold else 'NO'

assert cancel_or_nah(3, [-1, -3, 4, 2]) == 'YES'
assert cancel_or_nah(2, [0, -1, 2, 1]) == 'NO'
print 'OK'
