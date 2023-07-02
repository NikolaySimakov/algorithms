q = []
ans = []

def double(arr):
    res = []
    for v in arr:
        res += [v, v]
    return res

for _ in range(int(input())):
    inp = input()
    
    if inp[0] == '1':
        _, v = map(int, inp.split())
        q.append(v)
    elif inp[0] == '2':
        q = double(q)
    elif inp[0] == '3':
        v = q.pop(0)
        ans.append(v)

for v in ans:
    print(v)