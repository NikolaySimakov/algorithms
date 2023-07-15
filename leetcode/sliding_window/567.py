from collections import Counter

'''
Solution is same to Leetcode 438
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
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

