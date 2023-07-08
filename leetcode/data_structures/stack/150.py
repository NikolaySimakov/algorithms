from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if not tokens[i].isdigit() and not tokens[i][1:].isdigit():
                v2 = stack.pop()
                v1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(v1 + v2)
                elif tokens[i] == '-':
                    stack.append(v1 - v2)
                elif tokens[i] == '*':
                    stack.append(v1 * v2)
                elif tokens[i] == '/':
                    stack.append(int(v1 / v2))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]