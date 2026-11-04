class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        currMax = float("-inf")
        l = 0 

        for r in range(len(nums)):
            currMax = max(currMax, nums[r])
            while r - l + 1 > k:
                if nums[l] == currMax:
                    currMax = max(nums[l + 1:r + 1])
                l += 1
            if r - l + 1 == k:
                res.append(currMax)

        return res