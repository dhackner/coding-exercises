def string_permutations(input_str):
    if input_str is None or len(input_str) == 0:
        return []
    if len(input_str) == 1:
        return [input_str]
    ret_list = []
    for index in range(len(input_str)):
        current, remainder = input_str[index], input_str[:index] + input_str[index + 1:]
        for permutation in string_permutations(remainder):
            ret_list.append(current + permutation)

    return ret_list


"""
e.g.
'' []
'a' ['a']
'ab' 'a'('b') + 'b'('a')
'abc' 'a'('bc') + 'b'('ac') + 'c'('ab')
"""

assert set(string_permutations('a')) == set(['a'])
assert set(string_permutations('ab')) == set(['ab', 'ba'])
assert set(string_permutations('ab')) != set(['de'])
assert set(string_permutations('abc')) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print 'OK'
