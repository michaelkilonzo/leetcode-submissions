class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        min_len = float("inf")
        curr_sum = 0 
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target: 
                curr_sum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1
            
        if min_len == float("inf"):
            return 0
        else:
            return min_len