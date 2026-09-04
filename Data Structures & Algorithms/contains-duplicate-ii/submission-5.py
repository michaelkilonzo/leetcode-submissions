class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0 
        seen = set() 

        for j in range(len(nums)):
            # sliding window too large
            if j - i > k:
                seen.remove(nums[i])
                i += 1
            # duplicate found window and j - i <= k
            if nums[j] in seen and j - i <= k:
                return True
            seen.add(nums[j])
        
        return False
