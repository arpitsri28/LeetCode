class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        if n <= m:
            r = n
        else:
            r = m
        return_str = ""
        for k in range(r):
            return_str += word1[i] 
            return_str += word2[j]
            i += 1
            j += 1
        if n > m:
            return_str += word1[i:n]
        else:
            return_str += word2[j:m]
        return return_str
        