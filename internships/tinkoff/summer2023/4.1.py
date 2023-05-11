# ?

n = int(input())
a = list(map(int, input().split()))

freq = {}
boring = False
l = 2

while not boring and l <= n:
    freq.clear()
    for i in range(l):
        freq[a[i]] = freq.get(a[i], 0) + 1

        for i in range(l, n):
            freq[a[i-l]] -= 1
            if freq[a[i-l]] == 0:
                del freq[a[i-l]]
                freq[a[i]] = freq.get(a[i], 0) + 1

                counts = list(freq.values())
                if max(counts) - min(counts) <= 1:
                    boring = True
                    break

l += 1

print(l-1)
