class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)
        sc1 = sc2 = 0
        len_ = len(s1)
        s1.sort()
        s2.sort()

        for i in range(len(s1)):
            if s1[i] > s2[i]:
                sc1 += 1
            elif s1[i] < s2[i]:
                sc2 += 1
            else:
                sc1 += 1
                sc2 += 1
        
        return sc1 == len_ or sc2 == len_