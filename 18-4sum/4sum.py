class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            t = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            for j in range(j, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t2 = nums[j]
                l = j + 1
                r = n - 1
                while l < r:
                    if (nums[l] + nums[r] + t + t2) > target:
                        r -= 1
                    elif (nums[l] + nums[r] + t + t2) < target:
                        l += 1
                    else:
                        arr = [nums[l], nums[r], t, t2]
                        res.append(arr)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                        l += 1
        return res
        