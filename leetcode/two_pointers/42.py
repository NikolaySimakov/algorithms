from typing import List

class Solution:
    
    # Approach: find max bar index
    def trap(self, height: List[int]) -> int:
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