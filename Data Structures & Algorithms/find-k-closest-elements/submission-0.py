class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = []
        for n in arr:
            diff = abs(n - x)
            diffs.append(diff)

        # sliding window on diffs to append k smallest to res
        # want to find window of size k with smallest sum  
        res = []
        minSum = float("inf")
        l, currSum = 0, 0

        for r in range(len(diffs)):
            currSum += diffs[r]
            while r - l + 1 > k:
                currSum -= diffs[l]
                l += 1
            if r - l + 1 == k and currSum < minSum: 
                minSum = currSum
                res = arr[l:r+1]

        return res