class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        n = len(s)
        i = 0
        while (i < n):
            char = s[i]
            if (char not in hashMap):
                if (t[i] in hashMap.values()):
                    return False
                hashMap[char] = t[i]
            else:
                if (hashMap[char] != t[i]):
                    return False
            i = i + 1
        
        return True

        