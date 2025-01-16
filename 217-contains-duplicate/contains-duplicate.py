class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        n = len(nums)
        new_n = len(new_nums)
        return (n != new_n)