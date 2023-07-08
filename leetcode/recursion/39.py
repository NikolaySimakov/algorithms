from typing import List

'''
Get list of combinations where sum == target
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        combs = []

        def comb(arr: List[int] = [], start_index: int = 0, cur_sum: int = 0):
            if cur_sum > target: return
            if cur_sum == target: combs.append(arr)

            for i in range(start_index, n):
                comb(arr + [candidates[i]], i, cur_sum + candidates[i])
            
        comb()
        return combs