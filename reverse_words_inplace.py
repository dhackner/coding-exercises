# Strings are immutable in python, so switch to a character array and operate by
# indexes

# Algorithm: Create a function to reverse a word in place. Run on the full
# string and then on each individual word


def reverse(input_string):
    if input_string is None:
        return None
    string_as_list = list(input_string)

    # Learning: When enumerating always remember the -1 to len
    first_letter, last_letter = 0, len(string_as_list) - 1

    while first_letter < len(string_as_list) and string_as_list[first_letter] == ' ':
        first_letter += 1
    # Learning: enumerate() is cleaner but trickier in an interview. Stay simple.
    while last_letter > 0 and string_as_list[last_letter] == ' ':
        last_letter -= 1
    reversed_string_as_list = reverse_word(string_as_list, first_letter, last_letter)
    # print reversed_string_as_list
    index = 0
    while index < len(reversed_string_as_list):
        if reversed_string_as_list[index] != ' ':
            # Start of word, begin scan to end of word
            start = index

            # Learning: Multi-part conditionals in loops need to check the length FIRST to avoid OOB errors
            while index < len(reversed_string_as_list) and reversed_string_as_list[index] != ' ':
                index += 1
            # Above loop ends when index = len or it has hit a space, so we
            # subtract 1 to get to the last letter
            reversed_string_as_list = reverse_word(reversed_string_as_list, start, index - 1)
            # print reversed_string_as_list
        index += 1
    return ''.join(reversed_string_as_list)


def reverse_word(input_word, start=0, end=None):
    if end is None:
        end = len(input_word) - 1
    word_as_list = list(input_word)
    while start < end:
        word_as_list[start], word_as_list[end] = word_as_list[end], word_as_list[start]
        start += 1
        end -= 1
    return ''.join(word_as_list)


assert reverse_word("ABCDEF") == "FEDCBA"
assert reverse("Dan Hackner wrote this") == "this wrote Hackner Dan"
assert reverse("Dan Hackner wrote this ") == "this wrote Hackner Dan "
assert reverse(" Dan Hackner wrote this ") == " this wrote Hackner Dan "
assert reverse(" Dan Hackner wrote this") == " this wrote Hackner Dan"
assert reverse("Dan") == "Dan"
assert reverse("") == ""
assert reverse(" ") == " "
assert reverse("  ") == "  "
assert reverse(None) is None
print 'OK'
