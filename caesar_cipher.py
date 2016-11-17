# https://www.hackerrank.com/challenges/caesar-cipher-1


def shift(string, shift_num):
    mapping = {}
    shift_num = shift_num % 26  # Should only bump by a real number of letters
    for letter_num in range(ord('a'), ord('z') + 1):
        if letter_num + shift_num > ord('z'):
            mapping[chr(letter_num)] = chr((letter_num + shift_num) % ord('z') + ord('a') - 1)
        else:
            mapping[chr(letter_num)] = chr((letter_num + shift_num))
    for letter_num in range(ord('A'), ord('Z') + 1):
        if letter_num + shift_num > ord('Z'):
            mapping[chr(letter_num)] = chr((letter_num + shift_num) % ord('Z') + ord('A') - 1)
        else:
            mapping[chr(letter_num)] = chr((letter_num + shift_num))
    return ''.join([mapping[letter] if letter in mapping else letter for letter in string])

assert shift('Daniel', 1) == 'Ebojfm'
assert shift('Daniel', 27) == 'Ebojfm'
assert shift('Daniel', 53) == 'Ebojfm'
assert shift('Daniel', 0) == 'Daniel'
assert shift('Daniel', 26) == 'Daniel'
assert shift('zZ', 2) == 'bB'
assert shift('middle-Outz', 2) == 'okffng-Qwvb'
print 'OK'
