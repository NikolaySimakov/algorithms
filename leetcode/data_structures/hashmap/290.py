from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = defaultdict(list), defaultdict(list)

        for idx, char in enumerate(pattern):
            d1[char].append(idx)

        for idx, word in enumerate(s.split()):
            d2[word].append(idx)
            
        return list(d1.values()) == list(d2.values())
    
# Test solution
solution = Solution()
pattern, s = "abba", "dog cat cat dog"
print(solution.wordPattern(pattern, s))