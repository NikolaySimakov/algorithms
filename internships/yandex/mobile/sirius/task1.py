string = input()

res = []


def splits(current, length, split=[]):
    if current == length:
        global res
        res += [split]
    for i in range(current + 1, length + 1):
        splits(i, length, split + [i])


splits(0, len(string))

res.sort(key=lambda item: len(item), reverse=True)

possible_strings = []

for split in res:
    previous_index = 0
    subs = set()
    wrong = False
    res_string = ''
    for index in split:
        if string[previous_index: index] in subs:
            wrong = True
            break
        res_string += string[previous_index: index] + '-'
        subs.add(string[previous_index: index])
        previous_index = index
    if wrong:
        continue
    if previous_index == len(string):
        possible_strings.append(res_string[:-1])

print(max([string.split() for string in possible_strings],
      key=lambda string: len(string))[0])
