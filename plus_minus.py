# https://www.hackerrank.com/challenges/plus-minus


def percentage_polarity(array):
    if array is None or len(array) < 1:
        return None
    pos, neg, total = 0.0, 0.0, len(array)
    for element in array:
        if element > 0:
            pos += 1
        elif element < 0:
            neg += 1
    return (
        '%6f' % (pos / total),
        '%6f' % (neg / total),
        '%6f' % ((total - pos - neg) / total),
    )

assert percentage_polarity(None) is None
assert percentage_polarity([]) is None
assert percentage_polarity([1]) == ('1.000000', '0.000000', '0.000000')
assert percentage_polarity([-4, 3, -9, 0, 4, 1]) == ('0.500000', '0.333333', '0.166667')
print 'OK'
