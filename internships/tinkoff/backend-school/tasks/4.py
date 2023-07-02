
def transform(v):
    if v <= 9:
        return v
    else:
        return transform(sum(map(int, list(str(v)))))

def mult(array):
    c = 1
    for v in array:
        c *= v
    return c

res = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    v = mult(list(range(a, b+1)))
    t = transform(v)
    res.append(t)


for i in res:
    print(i)
    
    