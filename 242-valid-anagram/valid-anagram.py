class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if (m != n):
            return False
        hashMap_N = {}
        for i in s:
            if i not in hashMap_N:
                hashMap_N[i] = 1
            else:
                hashMap_N[i] += 1
        for j in t:
            if j not in hashMap_N:
                return False
            else:
                hashMap_N[j] -= 1
                if hashMap_N[j] < 0:
                    return False
        
        return True
