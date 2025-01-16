class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        n = len(intervals)
        i = 0
        intervals.sort(key=lambda x: x[0])
        if (n == 1):
            return intervals
        while i < n:
            if (i != n-1):
                start_i = intervals[i][0]
                end_i = intervals[i][1]
                start_ni = intervals[i+1][0]
                end_ni = intervals[i+1][1]
                if (end_i >= start_ni):
                    intervals[i] = [min(start_i, start_ni), max(end_i, end_ni)]
                    intervals.pop(i + 1)
                    n = n - 1
                else:
                    i = i + 1
            else:
                i = i + 1
        return intervals

        