import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashDist = {}
        dists = []
        heapq.heapify(dists)
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(dists, (distance, point))
        
        n = k
        output = []
        while n > 0:
            distance, point = heapq.heappop(dists)
            output.append(point)
            n -= 1
        
        return output
            
        
        

        