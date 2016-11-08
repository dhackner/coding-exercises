# https://www.careercup.com/question?id=5100595952222208

# Implemented for <= 9 total messages. If needed to support more, you could
# simplify by just shaving another 2 characters off instead of doing the math.for
# each individual message. i.e. message 3/27 doesn't need to have the extra
# character that message 11/27 takes up.

def splitter(input_string):
    input_string = input_string.strip()
    max_msg_size = 25 - len('(#/#)')  # Need to account for the message number at the end of each string

    if len(input_string) > (max_msg_size * 9):
        raise Exception('Disallow strings so long that they require > 9 messages')
    splits = input_string.split(' ')
    messages = []
    for word in splits:
        if len(word) > max_msg_size:
            raise Exception('Individual word too long for a message!')

        if len(messages) == 0 or len(messages[-1]) + len(word) > max_msg_size:
            messages.append(word)  # New message
        else:
            messages[-1] += ' ' + word

    for index in range(len(messages)):
        messages[index] += '({}/{})'.format(index + 1, len(messages))

    return messages

try:
    splitter(''.join('some more words' * 50))
    assert False
except Exception as e:
    assert e.message == 'Disallow strings so long that they require > 9 messages'

try:
    splitter('abcdefghijklmnopqrstuvwxyz and some more words')
    assert False
except Exception as e:
    assert e.message == 'Individual word too long for a message!'

assert splitter('Hi Dan Hackner, your Uber is arriving now! Be sure that you are outside!') == [
    'Hi Dan Hackner, your(1/4)',
    'Uber is arriving now!(2/4)',
    'Be sure that you are(3/4)',
    'outside!(4/4)'
]
print 'OK'
