# https://www.hackerrank.com/challenges/circular-array-rotation


def query_shifted(array, right_shift, index):
    if array is None or len(array) == 0 or index >= len(array):
        return None
    offset_index = (index - right_shift) % len(array)
    return array[offset_index]

assert query_shifted([], 2, 0) is None
assert query_shifted([1, 2], 2, 5) is None
assert query_shifted([1, 2, 3], 0, 0) == 1
assert query_shifted([1, 2, 3], 2, 0) == 2
assert query_shifted([1, 2, 3], 2, 1) == 3
assert query_shifted([1, 2, 3], 2, 2) == 1
print 'OK'
