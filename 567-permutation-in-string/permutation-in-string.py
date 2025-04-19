class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        hashMap = {}
        for i in range(len(s1)):
            if s1[i] in hashMap:
                hashMap[s1[i]] += 1
            else:
                hashMap[s1[i]] = 1
        k = len(s1)
        L = 0
        windowMap = {}
        for R in range(len(s2)):
            if s2[R] in windowMap:
                windowMap[s2[R]] += 1
            else:
                windowMap[s2[R]] = 1
            if R - L + 1 > k:
                windowMap[s2[L]] -= 1
                if windowMap[s2[L]] == 0:
                    del windowMap[s2[L]]
                L += 1

            if windowMap == hashMap:
                return True
        return False

        