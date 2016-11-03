# https://leetcode.com/problems/count-and-say/
current = '1'

for _ in range(10):
    print current

    new_current = ''
    num_occurances = 1
    for index, value in enumerate(current):
        if index + 1 < len(current) and value == current[index + 1]:
            num_occurances += 1
        else:  # Dump out
            new_current += str(num_occurances) + value
            num_occurances = 1

    current = new_current
