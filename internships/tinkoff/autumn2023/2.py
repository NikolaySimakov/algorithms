from collections import Counter

st = dict(Counter(input()))

# s - 1
# h - 1
# e - 1
# r - 1
# i - 1
# f - 2

all_chars = 's' in st and 'h' in st and 'e' in st and 'r' in st and 'i' in st and 'f' in st

if all_chars:
    get_min = min(st['s'], st['h'], st['e'], st['r'], st['i'], st['f']/2)
    print(get_min)
else:
    print(0)
