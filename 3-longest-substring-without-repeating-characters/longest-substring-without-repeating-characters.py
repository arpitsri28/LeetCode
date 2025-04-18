class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        length = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            else:
                window.add(s[R])
                length = max (R-L+1, length)
        return length

        