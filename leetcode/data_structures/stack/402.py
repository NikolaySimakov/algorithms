class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            
            if stack or n != '0':
                stack.append(n)
        
        if k:
            stack = stack[0:-k]
        
        return ''.join(stack) or '0'


s = Solution()

k = 3
num = '1432219'
res = s.removeKdigits(num, k)
print(res)