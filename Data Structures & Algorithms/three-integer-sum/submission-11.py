class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate nums[i] 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -nums[i] # nums[j] + nums[k] == -nums[i]
            while l < r: 
                current = nums[l] + nums[r]
                if current < target: 
                    l += 1
                elif current > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate nums[l]
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicate nums[r]
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res 
