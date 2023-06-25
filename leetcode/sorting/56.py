from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0

        while i < len(intervals) - 1:
            s1, e1, s2, e2 = intervals[i][0], intervals[i][1], intervals[i+1][0], intervals[i+1][1]
            if e1 >= s2:
                if e2 >= e1:
                    intervals[i] = [s1, e2]
                intervals.pop(i+1)
            else:
                i += 1

        return intervals