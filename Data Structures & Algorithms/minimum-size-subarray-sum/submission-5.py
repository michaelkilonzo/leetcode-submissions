class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        currSum, l = 0, 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                currSum -= nums[l]
                minLen = min(minLen, r - l + 1)
                l += 1

        if minLen == float("inf"):
            return 0
        else:
            return minLen

