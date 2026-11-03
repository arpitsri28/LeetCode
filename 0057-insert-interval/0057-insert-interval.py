class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        interval = intervals
        interval.append(newInterval)
        interval.sort(key=lambda x: x[0])
        ptr = 0
        for i in range(len(interval)):
            if i == ptr:
                continue
            if interval[ptr][1] >= interval[i][0]:
                if interval[ptr][1] < interval[i][1]:
                    interval[ptr][1] = interval[i][1]
                interval[i][0] = -1
            else:
                ptr += 1
        
        output = []
        for i in interval:
            if i[0] != -1:
                output.append(i)
        
        return output