class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        mult = 1
        j = len(columnTitle) - 1
        while j >= 0:
            cur = (ord(columnTitle[j]) - 64) * mult
            res += cur
            mult *= 26
            j -= 1

        return res        