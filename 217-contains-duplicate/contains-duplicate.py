class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for i in hashMap:
            if hashMap[i] >= 2:
                return True
        
        return False