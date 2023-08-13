from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)

        resStart, resLen = 0, float('inf')
        left, right = 0, 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while (valid == len(need)):
                # update final res
                if right - left < resLen:
                    resLen = right - left
                    resStart = left
                
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                
        return "" if resLen == float('inf') else s[resStart : resStart + resLen]