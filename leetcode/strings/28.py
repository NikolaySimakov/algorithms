# wrong answer

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 0
        x = 0
        while i < len(haystack):
            if haystack[i:i+x+1] == needle[:x+1]:
                while x < len(needle):
                    x += 1
                if haystack[i:i+x] == needle:
                    return i
                i += x
            else:
                i += 1
            x = 0

        return -1


# Example
s = Solution()
index = s.strStr(
    haystack='mississippi',
    needle='issi'
)
print(index)
