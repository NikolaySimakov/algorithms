class Solution:
    def scoreOfParenthesesStack(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(1, 2 * v)
            
        return stack[-1]
    
    def scoreOfParenthesesTwoPointers(self, s: str) -> int:
        count = t = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                t += 1
            elif s[i-1] == '(':
                count += 1 << t
                t -= 1
            else:
                t -= 1
        
        return count