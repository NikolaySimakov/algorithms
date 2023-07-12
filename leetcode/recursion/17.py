from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        combs = []

        def comb(c='', idx=0):
            if idx == n:
                if c: combs.append(c)
            else:
                for char in d[digits[idx]]:
                    comb(c + char, idx+1)
        
        comb()
        return combs