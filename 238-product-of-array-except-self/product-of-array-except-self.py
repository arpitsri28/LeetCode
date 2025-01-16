class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_p = 1
        j = len(nums) - 1
        product_s = 1
        results = [1] * n
        for i in range(n):
            results[i] = product_p
            product_p = product_p * nums[i]
        while j >= 0:
            results[j] = results[j] * product_s
            product_s = product_s * nums[j]
            j = j - 1
        return results
