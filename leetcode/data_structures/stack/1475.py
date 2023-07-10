from typing import List

'''
Use monotonic stack to save indexes 
save answer if price[stack[-1]] >= price[i] at index = stack[-1]
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # monotonic stack
        answer = prices

        for i, val in enumerate(prices):
            while stack and prices[stack[-1]] >= val:
                idx = stack.pop()
                answer[idx] = prices[idx] - val
            stack.append(i)
        
        return answer