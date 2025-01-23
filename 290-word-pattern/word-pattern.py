class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashMap = {}
        i = 0
        n = len(pattern)
        m = len(words)
        if (n != m):
            return False
        for p in pattern:
            if p not in hashMap:
                if words[i] in hashMap.values():
                    return False
                hashMap[p] = words[i]
            else:
                if hashMap[p] != words[i]:
                    return False
            i = i + 1
        
        return True
        