class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found_index = 0
        length = len(s)
        for i in t:
            if (found_index < length and i == s[found_index]):
                found_index = found_index + 1
        if(found_index == length):
            return True
        else:
            return False
        