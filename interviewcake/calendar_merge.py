# 4 - https://www.interviewcake.com/question/python/merging-ranges

# Algorithm: Mergesort, but when merging, if any two elements touch or overlap,
# merge them into a single element with min(start_times), max(end_times)

# Learning: Don't ultra-optimize yet, iterate towards the best solution

# Assumption: Well formed input of end > start


def calendar_mergesort(meeting_times):
    if meeting_times is None or len(meeting_times) <= 1:
        # Base case is 1 or 0
        return meeting_times
    halfway = len(meeting_times) // 2
    return merge(calendar_mergesort(meeting_times[:halfway]), calendar_mergesort(meeting_times[halfway:]))

# Learning: Enums for clarity
start, end = 0, 1


def merge(array1, array2):
    return_array = []
    idx1, idx2 = 0, 0
    while idx1 < len(array1) and idx2 < len(array2):
        elem1 = array1[idx1]
        elem2 = array2[idx2]

        # print '%s %s' % (elem1, elem2)

        # Learning: Stay calm with off-by-ones. Slowly examine each less than and greater than. Should it be equals as well? Does something need to fit more than one bound?

        # Explicit logic:
        # (A1, A2) (B1, B2) => if (B1 < A2 and B2 > A1) or (A1 < B2 and A2 > B1), return (min(A1, A2), max(B1, B2))
        # if elem1[start] <= elem2[end] and elem1[end] >= elem2[start] or\
            # elem2[start] <= elem1[end] and elem2[end] >= elem1[start]:
        min_start = min(elem1[start], elem2[start])
        max_start = max(elem1[start], elem2[start])
        min_end = min(elem1[end], elem2[end])
        max_end = max(elem1[end], elem2[end])
        # If overlap, merge
        if max_start <= min_end:
            return_array.append((min_start, max_end))
            idx1 += 1
            idx2 += 1

        # If no overlap, sort
        elif elem1[start] < elem2[start]:
            return_array.append(elem1)
            idx1 += 1
        elif elem2[start] < elem1[start]:
            return_array.append(elem2)
            idx2 += 1

        # Same start time
        else:
            if elem1[end] < elem2[end]:
                return_array.append(elem1)
                idx1 += 1
            elif elem2[end] < elem1[end]:
                return_array.append(elem2)
                idx2 += 1

    while idx1 < len(array1):
        if array1[idx1][start] <= return_array[-1][end]:
            return_array[-1] = (return_array[-1][start], max(array1[idx1][end], return_array[-1][end]))
        else:
            return_array.append(array1[idx1])
        idx1 += 1

    while idx2 < len(array2):
        if array2[idx2][start] <= return_array[-1][end]:
            return_array[-1] = (return_array[-1][start], max(array2[idx2][end], return_array[-1][end]))
        else:
            return_array.append(array2[idx2])
        idx2 += 1

    # Learning: Scaffold return statement immediately with function definition
    return return_array


def calendar_merge(meeting_times):
    # Provided solution from website
    if meeting_times is None or len(meeting_times) <= 1:
        # Base case is 1 or 0
        return meeting_times
    meeting_times = sorted(meeting_times)
    return_array = [meeting_times[0]]
    for current_start, current_end in meeting_times[1:]:
        if return_array[-1][end] >= current_start:
            return_array[-1] = (return_array[-1][start], max(return_array[-1][end], current_end))
        else:
            return_array.append((current_start, current_end))

    return return_array


assert calendar_mergesort(None) is None
assert calendar_mergesort([]) == []
assert calendar_mergesort([(1, 3)]) == [(1, 3)]
assert calendar_mergesort([(0, 1), (3, 5)]) == [(0, 1), (3, 5)]  # No overlap
assert calendar_mergesort([(0, 1), (1, 5)]) == [(0, 5)]  # Simple touch
assert calendar_mergesort([(0, 2), (1, 5)]) == [(0, 5)]  # Simple overlap
assert calendar_mergesort([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]  # Example case
assert calendar_mergesort([(1, 5), (2, 3)]) == [(1, 5)]
assert calendar_mergesort([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
assert calendar_mergesort([(1, 7), (2, 6), (3, 5), (7, 9)]) == [(1, 9)]

assert calendar_merge(None) is None
assert calendar_merge([]) == []
assert calendar_merge([(1, 3)]) == [(1, 3)]
assert calendar_merge([(0, 1), (3, 5)]) == [(0, 1), (3, 5)]  # No overlap
assert calendar_merge([(0, 1), (1, 5)]) == [(0, 5)]  # Simple touch
assert calendar_merge([(0, 2), (1, 5)]) == [(0, 5)]  # Simple overlap
assert calendar_merge([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]  # Example case
assert calendar_merge([(1, 5), (2, 3)]) == [(1, 5)]
assert calendar_merge([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]
assert calendar_merge([(1, 7), (2, 6), (3, 5), (7, 9)]) == [(1, 9)]
print 'OK'
