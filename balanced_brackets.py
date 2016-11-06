# https://www.hackerrank.com/challenges/ctci-balanced-brackets

# Algorithm: Each opening brace goes on a stack; whenever a closing brace is
# encountered, it must balance out the popped off top of the stack.


def is_matched(expression):
    closers = {'}': '{', ']': '[', ')': '('}
    open_stack = []
    for char in expression:
        if char not in closers:
            open_stack.append(char)
        else:
            if len(open_stack) == 0:
                return False  # Cannot close what wasn't opened
            open_stack, opener = open_stack[:-1], open_stack[-1]
            if opener != closers[char]:
                return False
    return len(open_stack) == 0


assert is_matched('{}()')
assert not is_matched('{()')
assert not is_matched('()}')
assert is_matched('{[()]}')
assert not is_matched('{[(])}')
assert is_matched('{{[[(())]]}}')
assert not is_matched('{{[[())]]}}')
print 'OK'
