# https://www.hackerrank.com/challenges/sherlock-and-pairs


def num(arr):
    counts = {}
    for element in arr:
        if element not in counts:
            counts[element] = 0
        counts[element] += 1
    return sum([n_2element_permutations(count) if count > 1 else 0 for element, count in counts.items()])


def n_2element_permutations(value):
    return value * (value - 1)  # N!/(N-K)!

# for x in range(int(raw_input())):
    # n = int(raw_input())
    # arr = map(int, raw_input().split(' '))
    # print num(arr)

assert num([1, 2, 3]) == 0
assert num([1, 1, 2]) == 2
assert num([1]) == 0
assert num([363, 916, 794, 363, 650, 387, 887, 336, 422, 363]) == 6
assert num([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 90

print 'OK'
