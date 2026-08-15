from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque([])
        l = 0
        r = 0
        count = 0
        if len(s) < 2:
            return len(s)
        while r < len(s):
            if s[r] not in dq:
                dq.append(s[r])
                r+=1
            else:
                count = max(count, len(dq))
                while s[l] != s[r] and len(dq) > 0:
                    dq.popleft()
                    l+=1
                dq.popleft()
                l+=1
        count = max(count, len(dq))
        return count
        
        