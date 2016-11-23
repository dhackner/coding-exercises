# https://www.hackerrank.com/challenges/flipping-the-matrix

# Learning: You don't need to actually do any flipping, just determine the max value possible for each position in the NxN matrix and sum them up

# Algorithm: Sum up the max of each position. The max for a given position [i][j]
# is max([i][j], [N-i][j], [i][N-j], [N-i][N-j])


def max_top_left_quadrant(array, N):
    if array is None or N == 0:
        return None
    total = 0
    max_bound = 2 * N - 1
    for i in range(N):
        for j in range(N):
            total += max(
                array[i][j],
                array[max_bound - i][j],
                array[i][max_bound - j],
                array[max_bound - i][max_bound - j],
            )
    return total

array = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]
assert max_top_left_quadrant(None, 2) is None
assert max_top_left_quadrant(array, 0) is None
assert max_top_left_quadrant(array, 2) == 414
print 'OK'

# for query in range(int(raw_input())):
    # N = int(raw_input())
    # array = [map(int, raw_input().split()) for i in range(2 * N)]
    # print max_top_left_quadrant(array, N)
