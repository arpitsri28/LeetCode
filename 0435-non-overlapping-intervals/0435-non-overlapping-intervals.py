class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        ptr = 0
        for i in range(len(intervals) - 1):
            if intervals[ptr][1] > intervals[i+1][0]:
                count += 1
            else:
                ptr = i + 1
        return count
            
        