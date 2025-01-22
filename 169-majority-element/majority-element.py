class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        r = n/2
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        for j in hashMap:
            if (hashMap[j] > r):
                return j
        