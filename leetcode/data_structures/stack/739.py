from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack:
                idx, t = stack[-1]
                if v - t > 0:
                    s = stack.pop()
                    res[idx] = i - idx
                else:
                    break
            
            stack.append((i, v))
        
        return res
