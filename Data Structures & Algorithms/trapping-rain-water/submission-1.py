class Solution:
    def trap(self, height: List[int]) -> int:
        # Total amount of water we have collected
        res = 0

        # Two pointers: one starts from each side
        l = 0
        r = len(height) - 1

        # Keep track of the tallest bar we've seen
        # from each direction.
        left_max = 0
        right_max = 0

        while l < r:
            # Ask yourself:
            # Which side should we process?
            #
            # Hint:
            # Compare height[l] and height[r].
            # Why does the shorter side give us useful information?
            if height[l] <= height[r]:
                # Update left_max if necessary.
                #
                # Question:
                # Is the current bar taller than our previous
                # tallest bar on the left?
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    # If the current bar is shorter than left_max,
                    # there may be water sitting above it.
                    #
                    # How much?
                    # Think:
                    #
                    #     water = water_level - height[l]
                    #
                    # What should water_level be?
                    res += left_max - height[l]

                # Move the left pointer
                l += 1

            else:

                # Same idea, but from the right.
                #
                # Update right_max if necessary.
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    # How much water sits above height[r]?
                    res += right_max - height[r]

                # Move the right pointer
                r -= 1

        return res