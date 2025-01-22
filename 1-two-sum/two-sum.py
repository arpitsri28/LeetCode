class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        i = 0
        for num in nums:
            diff = target - num
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[num] = i
            i += 1


        