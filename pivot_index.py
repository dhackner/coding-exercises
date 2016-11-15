# https://www.careercup.com/question?id=5695352763056128

# First pass: find the sum for each value of all values to its left. Then go
# from the right and sum until it matches the left sum for that index.

# Second pass: Take the grand sum of the values and iterate through the array
# subtracting each one from the grand sum and adding it to a second running sum. If
# the running sum == grand sum then that index is the pivot.


def find_pivot_index(array):
    grand_total = sum(array)
    running_sum = 0
    for index in range(len(array)):
        grand_total -= array[index]
        if running_sum == grand_total:
            return index
        else:
            running_sum += array[index]
    return -1

assert find_pivot_index([1, 2, 3, 4, 0, 6]) == 3
assert find_pivot_index([2, 4, 0, 6]) == 2
assert find_pivot_index([2, 4, 0]) == -1
print 'OK'
