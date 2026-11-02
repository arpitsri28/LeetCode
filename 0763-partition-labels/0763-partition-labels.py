class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = i
        parts = []
        end = 0
        start = 0
        for i in range(len(s)):
            last_o = hash_map[s[i]]
            end = max(last_o, end)
            if end == i:
                l = end - start + 1
                parts.append(l)
                start = i + 1
        
        return parts
            



        