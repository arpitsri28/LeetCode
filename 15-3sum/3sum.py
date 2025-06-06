class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            l = i + 1
            r = n-1
            while l < r:
                if (nums[l] + nums[r] + target) > 0:
                    r -= 1
                elif (nums[l] + nums[r] + target) < 0:
                    l += 1
                else:
                    arr = [nums[l], nums[r], target]
                    res.append(arr)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                    l += 1
        return res
                