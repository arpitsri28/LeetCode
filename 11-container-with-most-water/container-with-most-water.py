class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0
        l = 0
        r = n - 1
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            max_water = max(max_water, area)
            if (height[l] <= height[r]):
                l += 1
            elif (height[l] > height[r]):
                r -= 1
        return max_water