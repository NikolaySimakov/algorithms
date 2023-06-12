from typing import List

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        
        for i in range(len(nums) - 2):
            first_number = nums[i]
            k = len(nums) - 1
            j = i + 1
            
            while j < k:
                second_number = nums[j]
                third_number = nums[k]
                sm = first_number + second_number + third_number
                
                if sm > 0:
                    k -= 1
                elif sm < 0:
                    j += 1
                else:
                    triplets.add((first_number, second_number, third_number))
                    j += 1
                    k -= 1
        
        return triplets
    
    def threeSumSkipDuplicates(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        i = 0
        
        while i < len(nums) - 2:
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            # if nums[i] > 0, nums[i] + nums[j] + nums[k] > 0
            if nums[i] > 0:
                break
            
            first_number = nums[i]
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                second_number = nums[j]
                third_number = nums[k]
                
                sm = first_number + second_number + third_number
                
                if sm > 0:
                    k -= 1
                elif sm < 0:
                    j += 1
                else:
                    triplets.append([first_number, second_number, third_number])
                    j += 1
                    k -= 1
                    
                    # skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                
                    # skip duplicates
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
            i += 1
        
        return triplets
                    

                

s = Solution()

# Example
nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(res)