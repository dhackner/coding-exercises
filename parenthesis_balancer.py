# https://www.careercup.com/question?id=5734337711439872

values = {'(': 1, ')': -1}


def balances(pre, post, total):
    if total > 0:
        return None

    if len(post) == 0:
        # Done
        if total == 0:
            return [pre]
        else:
            return None
    if post[0] == '*':
        returnList = []
        balance = balances(pre, post[1:], total)
        if balance is not None:
            returnList += balance
        balance = balances(pre, '(' + post[1:], total)
        if balance is not None:
            returnList += balance
        balance = balances(pre, ')' + post[1:], total)
        if balance is not None:
            returnList += balance

        return returnList
    else:
        return balances(pre + post[0], post[1:], total - values[post[0]])


assert len(set(balances('', '(*(*)*)', 0))) == 5
assert len(set(balances('', '*(*(**)*', 0))) == 9

print 'OK'
