class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        piles.sort()
        n = len(piles)
        res = r 
        while l <= r:
            k = (l + r) // 2
            hrs = sum((pile + k - 1) // k for pile in piles) 
            if hrs <= h:
                res = k
                r = k - 1  
            else:
                l = k + 1  
        return res
                    
                