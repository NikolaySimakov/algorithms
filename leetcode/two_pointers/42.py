from typing import List

class Solution:
    
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ml, mr = height[l], height[r]
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                ml = max(ml, height[l])
                res += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                res += mr - height[r]
            
        return res
    
    # Approach: find max bar index
    def trapMaxBar(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = max_bar_idx = 0

        for i, v in enumerate(height):
            if v > height[max_bar_idx]:
                max_bar_idx = i
        
        for i in range(1, max_bar_idx):
            if height[l] > height[i]:
                res += height[l] - height[i]
            else:
                l = i
        
        for i in range(len(height) - 2, max_bar_idx, -1):
            if height[r] > height[i]:
                res += height[r] - height[i]
            else:
                r = i
        
        return res