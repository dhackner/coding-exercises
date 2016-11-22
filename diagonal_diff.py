# https://www.hackerrank.com/challenges/diagonal-difference

# Algorithm: Maintain two sums and multiply them by the first and last element
# respectively, increase the row, move the indexes in one element closer, and do
# it again.


def diagonal_diff(array):
    sum1, sum2 = 0, 0
    N = len(array[0])  # All rows are the same length, it is N x N
    idx1, idx2 = 0, N - 1
    for row in array:
        sum1 += row[idx1]
        sum2 += row[idx2]
        idx1 += 1
        idx2 -= 1
    return abs(sum1 - sum2)

input_array = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

assert diagonal_diff(input_array) == 15
print 'OK'
