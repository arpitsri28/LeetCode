class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = len(nums)
        prefix = []
        postfix = [0] * i
        total = 0
        for n in nums:
            prefix.append(total)
            total += n
        i -= 1
        total = 0
        while i >= 0:
            postfix[i] = total
            total += nums[i]
            i = i - 1
        i = len(nums)
        return_val = -1
        for j in range(i):
            if (prefix[j] == postfix[j]):
                return_val = j
                break
        
        return return_val
