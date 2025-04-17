class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        least = -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l += 1
            else:
                r -= 1
        least = l
        if nums[least] == target:
            return least
        elif nums[least] < target and target <= nums[-1]:
            l = least
            r = len(nums) - 1
        else:
            l = 0
            r = least - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
            else:
                return mid
        return -1
        