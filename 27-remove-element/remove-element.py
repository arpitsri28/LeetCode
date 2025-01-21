class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        n = len(nums)
        for i in range(n):
            if (nums[i] != val):
                temp.append(nums[i])
        k = len(temp)
        nums[:k] = temp
        return k
        