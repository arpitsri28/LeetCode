class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        hashMap = {}
        i = 0
        for num in nums:
            hashMap[num] = i
            i += 1
        res = -1
        for k in hashMap:
            if (hashMap[k] != k):
                res = hashMap[k]
                break
        
        if (res == -1):
            res = len(nums)
        
        return res
        