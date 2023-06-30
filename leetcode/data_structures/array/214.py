class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        p = s[::-1]
        add = ''

        for i in range(n):
            pp = p[i:]
            ss = s[:n-i]

            if pp != ss:
                add += p[i]
            else:
                break

        return add + s