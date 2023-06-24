from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        a = b = 0
        res = []

        while a < len(firstList) and b < len(secondList):
            s1, s2, e1, e2 = firstList[a][0], secondList[b][0], firstList[a][1], secondList[b][1]

            if s1 > e2: b += 1
            elif s2 > e1: a += 1
            else:
                interval = [max(s1, s2)]

                if e1 == e2:
                    interval.append(e1)
                    a += 1
                    b += 1
                elif e1 < e2:
                    interval.append(e1)
                    a += 1
                else:
                    interval.append(e2)
                    b += 1
                
                res.append(interval)
        
        return res