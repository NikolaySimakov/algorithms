from typing import List

'''
Using Two Pointers to solve task:
[a, a, a, b, b, c, c, c, c] -> [a, 3, b, 2, c, 4]
[b, b, b, b, b, b, b, b, b, b, b] -> [b, 1, 1]
With constant extra space

based on Leetcode 26
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        left = 0

        for right in range(1, len(chars) + 1):
            if right < len(chars) and chars[right-1] == chars[right]:
                count += 1
            else:
                chars[left] = chars[right-1]
                left += 1
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                count = 1

        return left