class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 1
        ptr = 0
        for i in range(len(points) - 1):
            if points[i+1][0] > points[ptr][1]:
                arrows += 1
                ptr = i + 1
        
        return arrows

#[[10,16],[2,8],[1,6],[7,12]]
#[[1,6], [2,8], [7,12], [10,16]]  