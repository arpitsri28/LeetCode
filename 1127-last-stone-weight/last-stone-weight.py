import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = stones
        for i in range(len(arr)):
            arr[i] *= -1
        
        heapq.heapify(arr)
        while len(arr) > 1:
            stone1 = heapq.heappop(arr)
            stone2 = heapq.heappop(arr)
            if stone1 != stone2:
                new_stone = abs(stone1-stone2) * -1
                heapq.heappush(arr, new_stone)
        
        if len(arr) == 0:
            return 0
        
        return arr[0] * -1


        