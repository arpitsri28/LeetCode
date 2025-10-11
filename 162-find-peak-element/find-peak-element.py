class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return 0
        while l < r:
            mid = (l + r) // 2
            left = nums[mid - 1] if mid - 1 >= 0 else nums[mid - 1] - 1
            right = nums[mid + 1] if mid + 1 < len(nums) else nums[mid + 1] - 1
            if nums[mid] > left and nums[mid] > right:
                return mid
            else:
                if nums[mid + 1] > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        
        return l
        