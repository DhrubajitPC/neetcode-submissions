class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        palindrome = 1

        for i in range(len(s) - 1):
            evenPal = self.expandFromCenter(s, i, i + 1)
            oddPal = self.expandFromCenter(s, i, i)
            palindrome += evenPal + oddPal
        return palindrome

    def expandFromCenter(self, s, left, right) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count+=1
        return count
