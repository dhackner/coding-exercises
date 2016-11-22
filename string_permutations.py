def recursive_string_permutations(input_str):
    if input_str is None or len(input_str) == 0:
        return set([''])
    ret_list = []
    for index, current in enumerate(input_str):
        remainder = input_str[:index] + input_str[index + 1:]
        for permutation in recursive_string_permutations(remainder):
            ret_list.append(current + permutation)

    return set(ret_list)


def iterative_string_permutations(input_str):
    if input_str is None:
        return set([''])

    stack = [('', input_str)]
    results = set([])
    while len(stack) > 0:
        # print '%s --- %s' % (stack, results)
        (permutation, remainder) = stack.pop()
        if len(remainder) == 0:
            results.add(permutation)
        else:
            for index, letter in enumerate(remainder):
                stack.append((letter + permutation, remainder[:index] + remainder[index + 1:]))

    return results

"""
e.g.
'' []
'a' ['a']
'ab' 'a'('b') + 'b'('a')
'abc' 'a'('bc') + 'b'('ac') + 'c'('ab')
"""

assert recursive_string_permutations(None) == set([''])
assert recursive_string_permutations('a') == set(['a'])
assert recursive_string_permutations('ab') == set(['ab', 'ba'])
assert recursive_string_permutations('ab') != set(['de'])
assert recursive_string_permutations('abc') == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

assert iterative_string_permutations(None) == set([''])
assert iterative_string_permutations('a') == set(['a'])
assert iterative_string_permutations('ab') == set(['ab', 'ba'])
assert iterative_string_permutations('ab') != set(['de'])
assert iterative_string_permutations('abc') == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print 'OK'
