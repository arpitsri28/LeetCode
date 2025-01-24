class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashS = {}
        for i in s:
            if i not in hashS:
                hashS[i] = 1
            else:
                hashS[i] += 1
        
        for j in t:
            if j not in hashS:
                return j
            else:
                if (hashS[j] > 0) :
                    hashS[j] -= 1
                else:
                    return j