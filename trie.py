# https://www.hackerrank.com/challenges/ctci-contacts

"""
Algorithm:
    Simulate a trie with a bunch of nested dictionaries.
    TODO | Improve by keeping words together and only splitting when matches deviate.
"""


lookup_trie = {}


def encode(word):
    current_level = lookup_trie
    for letter in word:
        if letter not in current_level:
            current_level[letter] = {}
        current_level = current_level[letter]

    current_level[None] = None  # Mark as terminating


def find(partial):
    current_level = lookup_trie
    for letter in partial:
        if letter not in current_level:
            return 0
        current_level = current_level[letter]

    return length(current_level)


def length(current_level):
    if current_level is None:
        return 1
    return sum([length(current_level[letter]) for letter in current_level])

encode('daniel')
encode('danielr')
encode('dan')
# print lookup_trie
assert find('dan') == 3
assert find('d') == 3
assert find('dani') == 2
assert find('x') == 0
