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