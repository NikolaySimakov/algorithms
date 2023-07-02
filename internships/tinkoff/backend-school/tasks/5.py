n = int(input())

lines = [input() for _ in range(n)]

def calc_counts(s):
    n_a = n_b = n_c = 0
    for c in s:
        if c == 'a':
            n_a += 1
        elif c == 'b':
            n_b += 1
        elif c == 'c':
            n_c += 1
    return n_a, n_b, n_c

def force(s):
    n_a, n_b, n_c = calc_counts(s)
    return n_a + n_b + n_c

def ugliness(s):
    n_a, n_b, n_c = calc_counts(s)
    return max(n_a, n_b, n_c) - min(n_a, n_b, n_c)


def backtracking(s='', max_force = 0, index=0):
    min_ugliness = float('inf') if s == '' else ugliness(s)
    if index == n: return force(s), min_ugliness
    
    max_force_1, min_ugliness_1 = backtracking(s + lines[index], max(max_force, force(s + lines[index])), index + 1)
    max_force_2, min_ugliness_2 = backtracking(s, max(max_force, force(s)), index + 1)
    
    if min_ugliness_1 <= min_ugliness:
        max_force = max(max_force_1, max_force)
        min_ugliness = min_ugliness_1
    
    if min_ugliness_2 <= min_ugliness:
        max_force = max(max_force_2, max_force)
        min_ugliness = min_ugliness_2
    
    return max_force, min_ugliness

print(backtracking()[0])

# ababaaaabbbbcc
# abcaaaccbb
# ababbbba