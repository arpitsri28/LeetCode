class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        windowMap = {}
        for R in range(len(s)):
            if s[R] in windowMap:
                windowMap[s[R]] += 1
            else:
                windowMap[s[R]] = 1
            max_char = max(windowMap, key=windowMap.get)
            max_val = windowMap[max_char]
            if (R - L + 1 - max_val) <= k:
                res = max(res, R - L + 1)
            else:
                windowMap[s[L]] -= 1
                L += 1
        return res