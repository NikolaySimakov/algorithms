from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n = len(s)
        lastSeen = {}

        for i in range(n):
            lastSeen[s[i]] = i
        
        l = []
        cur = tmp = 0

        for i in range(n):
            tmp += 1
            cur = max(cur, lastSeen[s[i]])

            if cur == i:
                l.append(tmp)
                tmp = 0
        
        return l