class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        n = len(unique)
        nums[:n] = unique
        return n

        