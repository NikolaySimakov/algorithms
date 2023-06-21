from collections import Counter
from typing import List

class Solution:
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        task_count = dict(Counter(tasks))
        max_count = max(task_count.values())
        max_tasks = sum(1 for count in task_count.values() if count == max_count)
        return max((max_count - 1) * (n + 1) + max_tasks, len(tasks))


s = Solution()
tasks = ["A","A","A","B","B","B","C","D","D"]
n = 2
print(s.leastInterval(tasks, n))