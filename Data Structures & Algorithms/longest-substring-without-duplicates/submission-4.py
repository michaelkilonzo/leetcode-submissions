class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0 
        seen = set() 
        

        for r in range(len(s)):
            # increment l ptr until current window has no duplicates
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)


        return res 