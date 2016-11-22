def merge_sort(string):
    if string is None or len(string) <= 1:
        return string
    string = list(string)
    half = len(string) // 2
    string = merge(merge_sort(string[:half]), merge_sort(string[half:]))
    return ''.join(string)

def merge(first, second):
    idx_1, idx_2 = 0, 0
    return_list = []
    while idx_1 < len(first) and idx_2 < len(second):
        if first[idx_1] < second[idx_2]:
            return_list.append(first[idx_1])
            idx_1 += 1
        else:
            return_list.append(second[idx_2])
            idx_2 += 1

    # Exhaust the remaining lists
    while idx_1 < len(first):
        return_list.append(first[idx_1])
        idx_1 += 1
    while idx_2 < len(second):
        return_list.append(second[idx_2])
        idx_2 += 1
    return return_list


assert merge_sort('ACB') == 'ABC'
assert merge_sort('ADFDDCB') == 'ABCDDDF'
print 'OK'
