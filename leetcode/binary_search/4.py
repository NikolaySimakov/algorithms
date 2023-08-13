from typing import List

class Solution:
    
    # Solution with complexity O(max(N, M))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0

        len1 = len(nums1)
        len2 = len(nums2)
        main = []

        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                main.append(nums1[i])
                i += 1
            else:
                main.append(nums2[j])
                j += 1
        
        while i < len1:
            main.append(nums1[i])
            i += 1
        
        while j < len2:
            main.append(nums2[j])
            j += 1

        if len(main) % 2 == 0:
            first = main[len(main)//2 - 1]
            second = main[len(main)//2]
            median = (first+second)/2
        else:
            median = main[len(main)//2]
        
        return median
    
    # TODO: write solution with O(log(n + m)) complexity