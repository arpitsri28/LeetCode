class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        product_p = 1
        j = len(nums) - 1
        product_s = 1
        i = 0
        while j >= 0 and i < n:
            suffix[j] = product_s
            product_s = product_s * nums[j]
            prefix[i] = product_p
            product_p = product_p * nums[i]
            j = j - 1
            i = i + 1

        results = [1] * n
        for k in range(n):
            results[k] = prefix[k] * suffix[k]
        
        return results