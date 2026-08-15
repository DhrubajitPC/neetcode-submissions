class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        size = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            total_length = sum(count.values())
            # print(total_length, count)
            while sum(count.values()) - max(count.values()) > k:
                # print(l, count)
                count[s[l]] -= 1
                size = max(size, sum(count.values()))
                l+=1
        size = max(size, sum(count.values()))
        return size
