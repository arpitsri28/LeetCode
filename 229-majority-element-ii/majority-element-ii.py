class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        result = []
        n = len(nums)
        r = n/3
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for i in hashMap:
            if hashMap[i]>r:
                result.append(i)
        
        return result

        