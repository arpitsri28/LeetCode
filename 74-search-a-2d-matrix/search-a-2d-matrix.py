class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l += 1
                elif nums[mid] > target:
                    r -= 1
                else:
                    return mid
            return -1
        n = len(matrix)
        for i in range(n):
            ret = search(matrix[i], target)
            if ret != -1:
                return True
        return False