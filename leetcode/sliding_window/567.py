from collections import Counter, defaultdict

'''
Solution is same to Leetcode 438
'''

class Solution:
    
    # Counter
    def checkInclusionCounter(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n, k = len(s2), len(s1)

        d1, d2 = Counter(s1), Counter(s2[:k-1])

        for i in range(k-1, n):
            if s2[i] in d2:
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
            
            if d2 == d1:
                return True
            
            if d2[s2[i - k + 1]] == 1:
                del d2[s2[i - k + 1]]
            else:
                d2[s2[i - k + 1]] -= 1
        
        return False
    
    # defaultdict
    def checkInclusionDefaultdict(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n, k = len(s2), len(s1)

        d1, d2 = defaultdict(int), defaultdict(int)

        for i in range(k):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        
        for i in range(k, n):
            if d1 == d2: return True
            d2[s2[i]] += 1
            d2[s2[i-k]] -= 1
            if d2[s2[i-k]] == 0:
                del d2[s2[i-k]]
        
        return d1 == d2

