class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        longestPal = s[0]

        for i in range(len(s) - 1):
            evenPal = self.expandFromCenter(s, i, i + 1)
            oddPal = self.expandFromCenter(s, i, i)
            longestPal = max(
                [longestPal, evenPal, oddPal], key=lambda val: len(val), default=""
            )
        return longestPal

    def expandFromCenter(self, s, left, right) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
