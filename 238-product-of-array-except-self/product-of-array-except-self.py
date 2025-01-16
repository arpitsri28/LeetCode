class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        product = 1
        for i in range(n):
            prefix[i] = product
            product = product * nums[i]

        j = len(nums) - 1
        product = 1
        while j >= 0:
            suffix[j] = product
            product = product * nums[j]
            j = j - 1

        results = [1] * n
        for k in range(n):
            results[k] = prefix[k] * suffix[k]
        
        return results