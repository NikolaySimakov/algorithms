from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = dict(Counter(s)), dict(Counter(t))
        return d1 == d2