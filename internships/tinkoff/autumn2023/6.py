from collections import defaultdict

n, m = map(int, input().split())
res = []
counter = defaultdict(int)
bands = dict()


class Band:
    def __init__(self, sp: set) -> None:
        self.s = sp
        
    def add(self, spirits: set) -> set:
        self.s |= spirits


for i in range(1, n+1):
    bands[i] = Band(set())
    bands[i].add(set([i]))
    counter[i] += 1


for _ in range(m):
    vals = list(map(int, input().split()))
    op = vals[0]
    if op == 1:
        a, b = vals[1], vals[2]
        if bands[a] != bands[b]:
            for spir in bands[a].s:
                counter[spir] += 1
                
            bands[a].add(bands[b].s)
            
            for spir in bands[b].s:
                counter[spir] += 1
                bands[spir] = bands[a]
            
    elif op == 2:
        a, b = vals[1], vals[2]
        res.append('YES' if bands[a] == bands[b] else 'NO') 
    else:
        a = vals[1]
        res.append(str(counter[a]))


for i in res:
    print(i)