class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while tail >= 0:
            if p1 < 0:
                nums1[tail] = nums2[p2]
                tail -= 1
                p2 -= 1
            elif p2 < 0:
                nums1[tail] = nums1[p1]
                tail -= 1
                p1 -= 1
            else:
                if nums1[p1] >= nums2[p2]:
                    nums1[tail] = nums1[p1]
                    tail -= 1
                    p1 -= 1
                elif nums1[p1] < nums2[p2]:
                    nums1[tail] = nums2[p2]
                    tail -= 1
                    p2 -= 1
        