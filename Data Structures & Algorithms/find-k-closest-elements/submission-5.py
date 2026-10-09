class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        minSum = float("inf")
        l, currSum = 0, 0

        for r in range(len(arr)):
            currSum += abs(arr[r] - x)
            while r - l + 1 > k: 
                currSum -= abs(arr[l] - x)
                l += 1
            if r - l + 1 == k and currSum < minSum:
                minSum = currSum 
                res = arr[l:r+1]
        
        return res 
