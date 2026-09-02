class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0

        while l < r:
            # find left boundary
            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    # calc water at l 
                    res += left_max - height[l]
                l += 1
            # find right boundary
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    # calc water at r
                    res += right_max - height[r]
                r -= 1

        return res