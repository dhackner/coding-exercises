# http://blog.gainlo.co/index.php/2016/04/08/if-a-string-contains-an-anagram-of-another-string/


def search(s, target):
    hash_of_s = set(s)
    for letter in target:
        if letter not in hash_of_s:  # Checks via hash, O(1)
            return False
    return True

assert search('adaainarelkjx', 'daniel')
assert not search('adaile', 'daniel')
print 'OK'
