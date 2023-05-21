days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

d, w = input().split()
ci = days.index(w)
d = int(d)
cur = 1


def f(a):
    return '.'+str(a) if a < 10 else str(a)


def aaa(ci, d):

    print(d, days[ci])

    cur = 1

    arr = [['..']*ci + [f(i) for i in range(1, 8-ci)]]
    cur += 7-ci

    while cur <= d:
        arr.append([f(i) for i in range(cur, cur + 7) if i <= d])
        cur += 7

    for i in arr:
        print(*i)


for i in range(28, 32):
    for j in range(7):
        aaa(j, i)
