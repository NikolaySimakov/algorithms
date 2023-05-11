_ = input()
s = input()

a = b = c = d = 0
distance = None

for i, char in enumerate(s):
    if char == 'a':
        a = i+1
    elif char == 'b':
        b = i+1
    elif char == 'c':
        c = i+1
    elif char == 'd':
        d = i+1

    if a and b and c and d:
        diff = max(a, b, c, d) - min(a, b, c, d) + 1
        distance = (min(diff, distance) if distance else diff)

print(distance if distance else -1)
