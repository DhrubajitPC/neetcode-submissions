from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) < 1:
            return ""
        
        c = Counter(t)
        l = 0
        res = [-1, -1]
        resLen = float('inf')
        have, need = 0, len(c)  # need = unique chars in t
        myMap = {}
        
        for r in range(len(s)):
            # Add right character to window
            myMap[s[r]] = myMap.get(s[r], 0) + 1
            
            # If we've matched the required count for this char
            if s[r] in c and myMap[s[r]] == c[s[r]]:
                have += 1
            
            # Try to shrink window from left
            while have == need:
                # Update result if this window is smaller
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Remove left character
                myMap[s[l]] -= 1
                if s[l] in c and myMap[s[l]] < c[s[l]]:
                    have -= 1
                l += 1
        
        if resLen == float('inf'):
            return ""
        
        l, r = res
        return s[l:r + 1]