class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMagazine = {}
        for m in magazine:
            if m not in hashMagazine:
                hashMagazine[m] = 1
            else:
                hashMagazine[m] += 1
        
        for r in ransomNote:
            if r in hashMagazine: 
                if (hashMagazine[r] > 0):
                    hashMagazine[r] -= 1
                else:
                    return False
            else:
                return False
        
        return True
        