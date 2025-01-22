class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        sortedVals = sorted(hashMap.items(), key=lambda item: item[1], reverse=True)[:k]
        res = []
        for i in sortedVals:
            res.append(i[0])
        return res
        