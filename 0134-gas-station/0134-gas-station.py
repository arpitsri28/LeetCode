class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        i = 0
        while i < n:
            if gas[i] >= cost[i]:
                start = i
                bal = 0
                visited = 0
                while bal >= 0 and visited < n:
                    bal = bal + gas[i] - cost[i]
                    if i == n - 1:
                        i = 0
                    else:
                        i += 1
                    visited += 1
                if i == start:
                    return i
                else:
                    i = start + visited
                    if i == n:
                        i = 0
            else:
                i += 1
        
        return -1
