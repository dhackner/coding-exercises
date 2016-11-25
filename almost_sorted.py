# https://www.hackerrank.com/challenges/almost-sorted


def almost_sorted_better(array):
    """ O(N)
    Algorithm: Scan elements. If in order, return yes. If element out of order,
    check for scan or swap.
    Swap: reserve the element, its before and its after. Keep going until another
    out of order element is hit. If the reserved element could fit here and this
    element could fit between the 'before' and 'after', return yes and the two
    indexces.
    Reverse: continuing the elements, they decrease and then increase again. If
    this only happens once then return yes, reverse + the start and end of this
    pattern. Special case, if start and end are next to each other, return as a
    swap instead.
    Else: return no.
    """
    # TODO | Error cases
    # previous_index = 0
    # index = 1
    # reserve_index = None
    # return_string = None

    # for index < len(array[1:]):
        # if array[index] >= array[previous_index]:
            # previous_index = index
            # index += 1
        # else:
            # if reserve_index is None:
                # if return_string is None:
                    # Begin tracking for a swap
                    # reserve_index = index
                # else:
                    # return 'no'
            # else:
                # if can_swap(reserve_index, index):
                    # return_string = 'yes\nswap %d %d' % (reserve_index+1, index+1)
                # else:
                    # return 'no'

    return ['yes']


# Learning: Brute force first, then discuss improvements!
def almost_sorted(original_array):
    """ O(NlogN)
    Compare the array to it's sorted version. If:
        same: return yes
        leftmost and rightmost change can swap and be sorted: return swap
        leftmost and rightmost change can reverse everything in between and be sorted: return reverse
        else: return no
    """
    sorted_array = sorted(original_array)
    if original_array == sorted_array:
        return 'yes'
    else:
        first_change = 0
        while sorted_array[first_change] == original_array[first_change]:
            first_change += 1
        last_change = len(original_array) - 1
        while sorted_array[last_change] == original_array[last_change]:
            last_change -= 1

        if original_array[first_change] == sorted_array[last_change] and\
                original_array[last_change] == sorted_array[first_change] and\
                original_array[first_change + 1:last_change] == sorted_array[first_change + 1:last_change]:
            # Two elements could swap but the inside of them remains the same,
            # then 'swap'
            return 'yes\nswap %d %d' % (first_change + 1, last_change + 1)
        else:
            if original_array[first_change:last_change + 1][::-1] == sorted_array[first_change:last_change + 1]:
                # Could reverse the inner section, then 'reverse'
                return 'yes\nreverse %d %d' % (first_change + 1, last_change + 1)
            else:
                return 'no'


# assert almost_sorted([2, 3]) == 'yes'
# assert almost_sorted([1, 4, 2, 5, 7, 8]) == 'yes\nswap 2 3'
# assert almost_sorted([1, 2, 4, 9, 3]) == 'no'  # Failed swap
# assert almost_sorted([3, 1, 2]) == 'no'
assert almost_sorted([1, 5, 4, 3, 2, 6]) == 'yes\nreverse 2 5'
print 'OK'
