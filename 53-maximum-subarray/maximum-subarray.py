class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            curSum = max(0, curSum)
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum
        