from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict(Counter(s))
        res = ''

        for val, count in sorted(d.items(), key=lambda item: item[1]):
            res += val * count

        return(res[::-1])