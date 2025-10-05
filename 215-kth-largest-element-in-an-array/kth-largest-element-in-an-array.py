import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums
        for i in range(len(arr)):
            arr[i] *= -1
        heap = heapq.heapify(arr)
        n = k
        while n > 0:
            curr = heapq.heappop(arr)
            n -= 1
        return curr*-1
        