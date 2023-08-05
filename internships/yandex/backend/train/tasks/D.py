n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(0)
else:
    print(n**(n-2) % (10**9 + 7))