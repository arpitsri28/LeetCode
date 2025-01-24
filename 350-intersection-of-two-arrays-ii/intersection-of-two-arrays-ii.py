class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap1 = {}
        hashMap2 = {}
        for num1 in nums1:
            if num1 not in hashMap1:
                hashMap1[num1] = 1
            else:
                hashMap1[num1] += 1
        
        for num2 in nums2:
            if num2 not in hashMap2:
                hashMap2[num2] = 1
            else:
                hashMap2[num2] += 1

        res = []
        for i in hashMap1:
            if i in hashMap2:
                n = min(hashMap1[i], hashMap2[i])
                for j in range(n):
                    res.append(i)
        
        return res
        