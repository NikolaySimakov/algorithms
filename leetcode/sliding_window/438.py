from typing import List
from collections import Counter

class Solution:
    
    # simple solution using collections.Counter
    def findAnagramsSimple(self, s: str, p: str) -> List[int]:

        n, k = len(s), len(p)
        p_counter = dict(Counter(p))
        res = []

        for i in range(n-k+1):
            s_counter = dict(Counter(s[i:i+k]))
            if s_counter == p_counter:
                res.append(i)
        
        return res
    
    # modified solutions (sliding window)
    def findAnagramsModified(self, s: str, p: str) -> List[int]:

        res = []
        n, k = len(s), len(p)
        s_counter, p_counter = dict(Counter(s[:k-1])), dict(Counter(p))

        for i in range(k-1, n):

            # add element to s_counter dict
            if s[i] in s_counter: s_counter[s[i]] += 1
            else: s_counter[s[i]] = 1

            # compare dicts
            if s_counter == p_counter:
                res.append(i - k + 1)
            
            # remove element from s_counter dict
            if s_counter[s[i - k + 1]] - 1 == 0: del s_counter[s[i - k + 1]]
            else: s_counter[s[i - k + 1]] -= 1
        
        return res