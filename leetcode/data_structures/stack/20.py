class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = [s[0]]

        for i in s[1:]:
            if stack and stack[-1] not in d.keys():
                return False
            if stack and i == d[stack[-1]]:
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0