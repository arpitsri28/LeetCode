class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        n = len(nums)
        for r in range(n):
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1
        for i in range(w, n):
            nums[i] = 0