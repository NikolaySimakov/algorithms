from typing import List

class Solution:
    
    # trivial solution, TLE on 57 test
    def taskSchedulerII_trivial(self, tasks: List[int], space: int) -> int:
        d, i, count = {}, 0, 0

        while i < len(tasks):
            if tasks[i] not in d.keys():
                d[tasks[i]] = count
                i += 1
            else:
                if count - d[tasks[i]] > space:
                    d[tasks[i]] = count
                    i += 1
            
            count += 1
        
        return count


    # right solution
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        d, curday = {}, 0

        for t in tasks:
            if t in d.keys():
                curday = max(d[t], curday)
            curday += 1
            d[t] = curday + space
        
        return curday


s = Solution()

# Example 1
tasks, space = [1,2,1,2,3,1], 3
print(s.taskSchedulerII(tasks, space))

# Example 1
tasks, space = [5,8,8,5], 2
print(s.taskSchedulerII(tasks, space))