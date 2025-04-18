class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        n = len(arr)
        total = 0
        qn = 0
        count = 0
        avg = 0
        for R in range(n):
            if R - L >= k:
                L += 1
            qn += 1
            total += arr[R]
            if qn == k:
                avg = total/qn
                if avg >= threshold:
                    count += 1
                qn -= 1
                total -= arr[R - k + 1]
                avg = 0
        return count

        