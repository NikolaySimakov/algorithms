class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = set()
        mx = 0

        for right in range(len(s)):
            v = s[right]
            while v in d:
                d.remove(s[left])
                left += 1
            d.add(v)
            mx = max(mx, right - left + 1)

        return mx


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
