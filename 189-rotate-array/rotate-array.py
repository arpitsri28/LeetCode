class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        rotation = nums[-k:]
        r = n - 1
        i = 0
        while r >= k-1:
            temp = nums[r]
            nums[r] = nums[r-k]
            r -= 1
        m = len(rotation)
        for i in range(m):
            nums[i] = rotation[i]
        


        