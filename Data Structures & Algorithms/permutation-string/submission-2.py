from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        windowLen = len(s1)
        l, r = 0, windowLen - 1
        while l <= len(s2) - windowLen:
            c2 = Counter(s2[l:r+1])
            # print(c1, c2)
            if c1 == c2:
                return True
            l+=1
            r+=1
        return False