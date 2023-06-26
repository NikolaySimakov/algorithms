from typing import List

class Solution:
    
    # backtracking + stack
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backtracking(open_ = 0, close_ = 0):
            if open_ == close_ == n:
                res.append(''.join(stack))
                return
            if open_ < n:
                stack.append('(')
                backtracking(open_ + 1, close_)
                stack.pop()
            if close_ < open_:
                stack.append(')')
                backtracking(open_, close_ + 1)
                stack.pop()

        backtracking()
        return res