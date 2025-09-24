class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest = 0

        for num in nums_set:                    
            if num - 1 not in nums_set:         
                curr = num
                length = 0
                while curr in nums_set:
                    length += 1
                    curr += 1
                if length > longest:
                    longest = length

        return longest