# https://www.careercup.com/question?id=5734337711439872

values = {'(': 1, ')': -1}


# Base cases:
# 1) negative total (more closes have happened then opens)
# 2) no letter left, total == 0 (valid string)
# 3) no letter left, total > 0 (invalid string due to hanging opens. this state
# is allowed while there are still letters left)
def balances(pre, post, total):
    if total < 0:
        # Learning: It is tempting to try to merge this case in with the one below. Spell out the definition of the base cases, so that you don't accidentally refactor them away.
        # Done | Invalid combo due to having more closes at any point then opens
        return []

    if len(post) == 0:
        if total == 0:
            # Done | Valid combo
            return [pre]
        else:
            # Done | Invalid combo due to uneven open parens
            return []
    if post[0] == '*':
        # Learning: Careful with array + vs array.append vs array.extend
        return [] + \
            balances(pre, post[1:], total) + \
            balances(pre, '(' + post[1:], total) + \
            balances(pre, ')' + post[1:], total)
    else:
        return balances(pre + post[0], post[1:], total + values[post[0]])


assert len(set(balances('', '(*(*)*)', 0))) == 5
assert len(set(balances('', '*(*(**)*', 0))) == 9

print 'OK'
